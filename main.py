"""
This module load and manage the ngrok tunnel.
"""

import argparse
import time
import os

from src.ngrok import start_ngrok, stop_ngrok


CRONJOB_NGROK_STATIC_DOMAIN = os.getenv('CRONJOB_NGROK_STATIC_DOMAIN', '')
CRONJOB_NGROK_DISABLE_LOCAL_SCHEDULE = bool(
        os.getenv('CRONJOB_NGROK_DISABLE_LOCAL_SCHEDULE', 'False')
    )

if CRONJOB_NGROK_DISABLE_LOCAL_SCHEDULE is False:
    import schedule

args = argparse.ArgumentParser(description='Run a scheduled task with ngrok tunneling.')
args.add_argument('--protocol',
                  type=str,
                  help='Protocol to use for ngrok (e.g., http, tcp)',
                  required=True)
args.add_argument('--port', type=int, help='Port number to forward through ngrok', required=True)
args.add_argument('--domain', type=str, help='Static domain given by ngrok to use', required=False)
args.add_argument('--minutes',
                  type=int,
                  help='The minutes to the ngrok stop and start again',
                  required=False,
                  default=60)

args = args.parse_args()

protocol = args.protocol
port = int(args.port)
domain = args.domain
minutes = int(args.minutes)


def execute():
    """
    Execute the scheduled task with ngrok tunneling.
    
    Returns:
        None
    """

    subprocess = None

    try:
        start_time = time.time()

        print('Executing scheduled task')

        subprocess = start_ngrok(protocol, port, domain)

        end_time = time.time()

        time_left_to_stop_ngrok = (60 * minutes) - (end_time - start_time) - 5

        time_formated = time.ctime(time_left_to_stop_ngrok + time.time())
        print(f'The ngrok process will terminate at "{time_formated}"')

        time.sleep(time_left_to_stop_ngrok)

        stop_ngrok(subprocess)
    except KeyboardInterrupt as e:
        print("Execution interrupted by user")
        stop_ngrok(subprocess)
        raise e
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        stop_ngrok(subprocess)

    finally:
        print("Execution completed")

if __name__ == '__main__':
    try:
        if domain is None:
            domain = CRONJOB_NGROK_STATIC_DOMAIN

        if CRONJOB_NGROK_DISABLE_LOCAL_SCHEDULE is False:
            schedule.every(minutes).minutes.do(execute)

        execute()

        if CRONJOB_NGROK_DISABLE_LOCAL_SCHEDULE is False:
            while True:
                schedule.run_pending()
                # The min time in seconds that the schedule can run(1 minute)
                time.sleep(60)
    except KeyboardInterrupt as e:
        print("User cancelled the execution")

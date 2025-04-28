"""
This module create the interface to communicate with ngrok.
"""

import subprocess

def start_ngrok(protocol: str, port: int, static_domain: str):
    """
    Start the ngrok tunneling process.
    
    Args:
        protocol (str): The protocol to use for the tunnel (e.g., 'http', 'tcp').
        port (int): The local port to forward.
        static_domain (str): The custom domain to use for the tunnel.
        
    Returns:
        subprocess.Popen: The ngrok subprocess.
    """
    print('Starting ngrok')

    ngrok_process = subprocess.Popen(['ngrok', protocol, f'--url={static_domain}', str(port)],
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE)

    print('Started ngrok')

    return ngrok_process

def stop_ngrok(ngrok_process):
    """
    Stop the ngrok process.
    
    Args:
        ngrok_process (subprocess.Popen): The ngrok subprocess to terminate.
    
    Returns:
        None
    """
    print('Stopping ngrok')

    ngrok_process.terminate()
    ngrok_process.wait()

    print('Stopped ngrok')

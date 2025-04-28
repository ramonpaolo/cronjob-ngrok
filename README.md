# Cronjob Ngrok

This script create and destroy the free tunnel service provided by ngrok, to always keep your local server online and accessible from the internet in the same domain(URL).

## Features

- **Scheduled Tasks**: Run tasks at specific intervals.
- **Ngrok Tunneling**: Create and delete ngrok tunnels dynamically.
- **Static Domain Support**: Use a static domain provided by ngrok.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ramonpaolo/cronjob-ngrok.git
```

2. Enter the project directory:
```bash
cd cronjob-ngrok
```

3. Install dependencies:
```bash
# It's recommended to use a virtual environment. You can create one with: "python -m venv .venv"
# source venv/bin/activate (Linux/Mac)
# venv\Scripts\activate (Windows)
# Then install the dependencies:
pip install -r requirements.txt
```

4. Define the method of execution:

The script can be executed directly with the default cron or scheduled using cronjob(crontab).

To use it directly, just run the code with the desired parameters. For example:

```bash
python main.py --protocol http --port 8080 --domain mydomain.ngrok-free.app --minutes 60
```

This will execute the script that will start an ngrok tunnel on port 8080 using the HTTP protocol and the static domain `mydomain.ngrok-free.app`. The tunnel will be stopped and started again every hour(each 60 minutes).

To schedule the script using cron, add a new line to your crontab file, for example:

> 0 * * * * /usr/bin/python3 /path/to/cronjob-ngrok/main.py

> [!WARNING]
> To use the script with the your own cronjob(crontab), you need to set the Environment Variable `CRONJOB_NGROK_DISABLE_LOCAL_SCHEDULE` to `True` in your workspace


## Environments and Arguments

The script can be configured using environment variables or command-line arguments. The following environment variables and arguments are available:

### Environments

- `CRONJOB_NGROK_STATIC_DOMAIN`: A static domain provided by ngrok that will be used for the tunnel.
- `CRONJOB_NGROK_DISABLE_LOCAL_SCHEDULE`: If set to True, the script will not use the local schedule module and will only run once. It's useful when using a cronjob or another scheduling tool.

### Arguments

- `--protocol`: **Required** - The protocol to use for ngrok (e.g., http, tcp).
- `--port`: **Required** - The port number to forward through ngrok.
- `--domain`: **Required** - A static domain provided by ngrok that will be used for the tunnel.
- `--minutes`: **Optinal** - Default value: 60 - The interval in minutes between stopping and starting the ngrok tunnel. Default is 60 minutes.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

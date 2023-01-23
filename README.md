# Python-bot
##Requirements:
- A Twilio account and a smartphone with an active phone number and WhatsApp installed.
- Must have Python 3.9 or newer installed in the system.
- Flask: We will be using a flask to create a web application that responds to incoming WhatsApp messages with it.
- ngrok: Ngrok will help us to connect the Flask application running on your system to a public URL that Twilio can connect to. This is necessary for the development version of the chatbot because your computer is likely behind a router or firewall, so it isn’t directly reachable on the Internet.

##Step 1: Preparation
- Get Ngrok and run `ngrok http 5000`
- Get Twilio account using Twilio WhatsApp API + connect with your phone

##Step 2: Installation
- Create an environment for the scripts: `mkdir python-bot && cd python-bot`
- Run and activate the environment: `python3 -m venv python-bot-env && source python-bot-env/bin/activate`
- Get all required libs: `pip3 install twilio flask requests beautifulsoup4`

##Step 3: Running the script
- Run `python3 bot.py`

##Step 3: Running the script
- Interact with the script using different messages:
1. `quote`: will randomly send a quote
2. `kat`: will send a cat picture
3. `wiki + <input>`: will send the specific wiki page
4. `http + <httpCode>`: will send a http cat picture 
5. `vacatures`: will send all job openings from www.conspect.nl



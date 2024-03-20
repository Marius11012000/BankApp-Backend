import requests
import json

NGROK_API_KEY = "2dPy6F8SVmqlj3mqRDJIoQhS520_7Ge87nmJaGFiHz2kn7wPx"
NGROK_API_URL = "https://api.ngrok.com/tunnels"
CONFIG_FILE_PATH = "C:/Users/Marius/Documents/Facultate/Final/app/src/main/res/raw/config.properties"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {NGROK_API_KEY}",
    "Ngrok-Version": "2"
}

# Obtine lista de tuneluri ngrok active
response = requests.get(NGROK_API_URL, headers=headers)
print(response.text)
tunnels = json.loads(response.text)['tunnels']
ngrok_url = None

# Cauta tunelul HTTP/S si obtine URL-ul public
for tunnel in tunnels:
    if tunnel['proto'] == 'https':
        ngrok_url = tunnel['public_url']
        break

if ngrok_url:
    # Actualizeaza fisierul de configurare cu noul URL ngrok
    with open(CONFIG_FILE_PATH, 'w') as file:
        file.write(f"ngrok_url={ngrok_url}\n")
    print(f"Updated ngrok URL to {ngrok_url} in {CONFIG_FILE_PATH}")
else:
    print("No HTTPS tunnel found.")
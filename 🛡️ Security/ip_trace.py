# ip_trace.py
# Consulta IP via API do ipinfo.io

import requests

ip = "8.8.8.8"
response = requests.get(f"https://ipinfo.io/{ip}/json")
print(response.json())

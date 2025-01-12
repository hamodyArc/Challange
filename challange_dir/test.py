import requests
import time
url = "https://api.coingecko.com/api/v3/simple/price?x_cg_demo_api_key=YOUR_API_KEY"

headers = {
    "accept": "application/json",
    "x-cg-demo-api-key": "CG-wR4GkJELFR14WZbS9w7CS8iV"
}

params = {
    'ids': 'ripple',
    'vs_currencies': 'usd',
    'precision': 3,
}
while True:
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    print(data)
    time.sleep(30)
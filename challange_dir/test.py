import requests

url = "https://pro-api.coingecko.com/api/v3/ping"

headers = {
    "accept": "application/json",
    "x-cg-pro-api-key": "CG-wR4GkJELFR14WZbS9w7CS8iV"
}

response = requests.get(url, headers=headers)

print(response.text)
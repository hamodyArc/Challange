import requests
import time
import json

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

headers = {
    'X-CMC_PRO_API_KEY': '0977c65a-4d09-4df0-872e-e6b97822c77a',
    'Accept': 'application/json',
}
params = {
    'start': '1',  
    'limit': '10',   
    'convert': 'USD', 
    'sort': 'market_cap', 
}
raw = []

while True: 
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    for coin in data['data']:
        if coin['symbol'] == 'XRP':
            print(coin['name'], coin['quote']['USD']['price'])
            current_quote = coin['quote']['USD']['price']
            raw.append(current_quote)
            if len(raw) > 14:
                raw.pop(0)
                gain = sum(max(raw[i] - raw[i - 1], 0) for i in range(1, len(raw))) / 14
                loss = sum(max(raw[i - 1] - raw[i], 0) for i in range(1, len(raw))) / 14
                print("Gain:", gain, "Loss:", loss)

                RS = gain / loss
                RSI = 100 - (100 / (1 + RS))
                print("Gain:", gain, "Loss:", loss, "RS:", RS, "RSI:", RSI)
            else:
                print("Not enough data to calculate RSI: ", len(raw), raw)
    time.sleep(61)

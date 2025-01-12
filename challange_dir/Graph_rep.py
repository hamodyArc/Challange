import requests
from datetime import datetime, timedelta
import time

headers = {
    "accept": "application/json",
    "x-cg-demo-api-key": "CG-wR4GkJELFR14WZbS9w7CS8iV"
}

days = []
raw = []

for i in range(14, 0, -1):
    currentDate = (datetime.now() - timedelta(days=i)).strftime("%d-%m-%Y")
    days.append(currentDate)

    url_history = f"https://api.coingecko.com/api/v3/coins/wrapped-xrp-universal/history?date={currentDate}&localization=false?x_cg_demo_api_key=YOUR_API_KEY"
    try:
        dateResponse = requests.get(url_history, headers=headers)
        dateResponse.raise_for_status() 
        data = dateResponse.json()

        if "market_data" in data and "current_price" in data["market_data"] and "usd" in data["market_data"]["current_price"]:
            current_price = data["market_data"]["current_price"]["usd"]
            raw.append(current_price)
            if len(raw) > 13:
                raw.pop(0)
                gain = sum(max(raw[i] - raw[i - 1], 0) for i in range(1, len(raw))) / 14
                loss = sum(max(raw[i - 1] - raw[i], 0) for i in range(1, len(raw))) / 14
                print("Gain:", gain, "Loss:", loss)

                RS = gain / loss
                RSI = 100 - (100 / (1 + RS))
                print("Gain:", gain, "Loss:", loss, "RS:", RS, "RSI:", RSI)
            else:
                print("Not enough data to calculate RSI: ", len(raw), raw)
        else:
            print(f"Data unavailable for {currentDate}")
            raw.append(None)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        raw.append(None)

    time.sleep(3)

print("Prices:", raw)

import requests
from datetime import datetime, timedelta
import time

# No API key is needed for CoinGecko's free API
headers = {
    "accept": "application/json",
    "x-cg-demo-api-key": "CG-wR4GkJELFR14WZbS9w7CS8iV"
}

days = []
raw = []

# Loop to get the last 14 days
for i in range(14, 0, -1):
    currentDate = (datetime.now() - timedelta(days=i)).strftime("%d-%m-%Y")
    days.append(currentDate)

    url_history = f"https://api.coingecko.com/api/v3/coins/wrapped-xrp-universal/history?date={currentDate}&localization=false?x_cg_demo_api_key=YOUR_API_KEY"
    print(i)
    try:
        # Make the API request
        dateResponse = requests.get(url_history, headers=headers)
        dateResponse.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        # Parse JSON response
        data = dateResponse.json()

        # Check if the required data exists
        if "market_data" in data and "current_price" in data["market_data"] and "usd" in data["market_data"]["current_price"]:
            current_price = data["market_data"]["current_price"]["usd"]
            raw.append(current_price)
        else:
            print(f"Data unavailable for {currentDate}")
            raw.append(None)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        raw.append(None)

    # Add a delay to avoid rate limiting
    time.sleep(3)

# Print the results
print("Prices:", raw)
print("Days:", days)

# This is Sentry.

# Day 1. June 2026.

# One wallet. One API call. One alert.

# Everything else is downstream of this working.

import requests

wallet = "0xYourWalletAddress"

api_key = "YourEtherscanKey"  # Free at etherscan.io

url = f"https://api.etherscan.io/api?module=account&action=txlist&address={wallet}&apikey={api_key}"

response = requests.get(url)

transactions = response.json()

print(transactions['result'][:5])

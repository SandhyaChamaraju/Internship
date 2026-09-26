import requests

def get_crypto_prices(coins):
    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": ",".join(coins),
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    return response.json()


coins = ["bitcoin", "ethereum", "solana", "dogecoin"]

prices = get_crypto_prices(coins)

for coin, data in prices.items():
    print(f"{coin.capitalize():10} ${data['usd']:,.2f}")

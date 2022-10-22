import requests
import json
import dotenv
import os


class Coin():
    def __init__(self, coin):
        self.coin = coin

    def get_currency(self, currency):
        dotenv.load_dotenv()
        API_KEY = os.getenv("API_KEY")
        url = f"https://min-api.cryptocompare.com/data/price?fsym={self.coin}&tsyms={currency}"

        req = requests.get(url, headers={'authorization': f'Apikey {API_KEY}'})

        curr = json.loads(req.text)
        return curr[f'{currency}']



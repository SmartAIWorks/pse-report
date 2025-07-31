import requests

from app.models.trading_asset import TradingAsset


class CryptoService:
    BASE_URL = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=__currency__&ids=__coin_id__"

    def get_asset_data(self, coin_id:str, currency_code: str = 'usd'):
        url = self.BASE_URL.replace('__currency__', currency_code).replace('__coin_id__', coin_id)
        response = requests.get(url)
        data = response.json()

        crypto_data = data[0]
        name = crypto_data["name"]
        code = crypto_data["symbol"]
        price = crypto_data["current_price"]
        currency = currency_code
        percent_change = crypto_data["price_change_percentage_24h"]
        volume = -1
        value = crypto_data["total_volume"]

        return TradingAsset(name = name
                     , code = code.upper()
                     , price= price
                     , currency= currency.upper()
                     , percent_change= percent_change
                     , volume= volume
                     , value= value)
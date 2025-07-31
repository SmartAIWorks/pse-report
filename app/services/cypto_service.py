import requests

from app.models.trading_asset import TradingAsset
from app.utils.trading_asset_helper import parse_asset_prices, calculate_price_change


class CryptoService:
    BASE_URL = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=__currency__&ids=__coin_id__"

    def get_asset_data(self, coin_id:str, currency_code: str = 'usd'):
        url = self.BASE_URL.replace('__currency__', currency_code).replace('__coin_id__', coin_id)
        response = requests.get(url)
        data = response.json()

        crypto_data = data[0]
        name = crypto_data["name"]
        code = crypto_data["symbol"].upper()
        price = crypto_data["current_price"]
        currency = currency_code
        percent_change = crypto_data["price_change_percentage_24h"]
        volume = -1
        value = crypto_data["total_volume"]

        asset_prices = parse_asset_prices()
        asset_price = asset_prices.get(code)
   
        percent_change_from_avg = calculate_price_change(asset_price, price) if asset_price else 0
       
        return TradingAsset(name = name
                     , code = code.upper()
                     , price= price
                     , currency= currency.upper()
                     , percent_change= percent_change
                     , percent_change_from_avg= percent_change_from_avg
                     , volume= volume
                     , value= value)
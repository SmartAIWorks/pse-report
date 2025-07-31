import requests
from app.models.trading_asset import TradingAsset
from app.utils.email_helper import PSE_EMAIL_TEMPLATE

class StockService:
    BASE_URL = f"http://phisix-api3.appspot.com/stocks/__CODE__.json"

    def get_stock_data(self, stock_code: str):
        url = self.BASE_URL.replace('__CODE__', stock_code)
        response = requests.get(url)
        data = response.json()

        stock_data = data["stock"][0]
        name = stock_data["name"]
        code = stock_data["symbol"]
        price = stock_data["price"]["amount"]
        currency = stock_data["price"]["currency"]
        percent_change = stock_data["percent_change"]
        volume = stock_data["volume"]
        value = volume * price

        return TradingAsset(name = name
                     , code = code.upper()
                     , price= price
                     , currency= currency.upper()
                     , percent_change= percent_change
                     , volume= volume
                     , value= value)

import requests
from app.models.trading_asset import TradingAsset
from app.utils.email_helper import PSE_EMAIL_TEMPLATE
from app.utils.trading_asset_helper import parse_asset_prices, calculate_price_change

class StockService:
    BASE_URL = f"http://phisix-api3.appspot.com/stocks/__CODE__.json"

    def get_stock_data(self, stock_code: str):
        url = self.BASE_URL.replace('__CODE__', stock_code)
        response = requests.get(url)
        data = response.json()

        stock_data = data["stock"][0]
        name = stock_data["name"]
        code = stock_data["symbol"].upper()
        price = stock_data["price"]["amount"]
        currency = stock_data["price"]["currency"]
        percent_change = stock_data["percent_change"]
        volume = int(round(stock_data["volume"]))
        value = int(round(volume * price))

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

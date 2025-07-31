from app.models.trading_asset import TradingAsset
from app.services.stock_service import StockService
from app.services.cypto_service import CryptoService
from app.utils.trading_asset_helper import buil_email_message

from app.config import EMAIL_API_KEY, STOCK_LIST, EMAIL_SENDER, EMAIL_RECIPIENT, COIN_LIST
from app.services.email_service import EmailService
from datetime import datetime
from zoneinfo import ZoneInfo

stock_service = StockService()
crypto_service = CryptoService()

def get_stock_data() -> list[TradingAsset]:
    stock_data: list[TradingAsset] = []
    for code in STOCK_LIST.split(','):
        result = stock_service.get_stock_data(code)
        stock_data.append(result)
    return stock_data

def get_crypto_data() -> list[TradingAsset]:
    trading_asset: list[TradingAsset] = []
    for code in COIN_LIST.split(','):
        result = crypto_service.get_asset_data(code)
        trading_asset.append(result)
    return trading_asset

def send_email(asset_data:list[TradingAsset]):
    email_content = buil_email_message(trading_assets = asset_data)
    email_service = EmailService()

    ph_time = datetime.now(ZoneInfo("Asia/Manila"))

    email_subject = f"PSE Summary - {ph_time.strftime("%Y-%m-%d %H:%M:%S")}"
    email_service.send_message(subject=email_subject
                            , message=email_content
                            , sender=EMAIL_SENDER
                            , receipient=EMAIL_RECIPIENT)

def run():
    stock_data = get_stock_data()
    coin_data =  get_crypto_data()

    trading_assets = stock_data + coin_data

    
   # print('st', stock_data)
    #print('cd', coin_data)
    print('ta', trading_assets)
    send_email(asset_data = trading_assets)


if __name__ == "__main__":
    run()
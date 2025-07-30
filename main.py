import sib_api_v3_sdk
from app.models.stock_model import Stock
from app.services.stock_service import StockService
from app.config import EMAIL_API_KEY, STOCK_LIST, EMAIL_SENDER, EMAIL_RECIPIENT
from app.services.email_service import EmailService
from datetime import datetime
from zoneinfo import ZoneInfo

stock_service = StockService()

def get_stock_data() -> list[Stock]:
    stock_data: list[Stock] = []
    for code in STOCK_LIST.split(','):
        result = stock_service.get_stock_data(code)
        stock_data.append(result)
    return stock_data

def send_email(stock_data:list[Stock]):
    email_content = stock_service.build_email_message(stock_data)
    email_service = EmailService()

    ph_time = datetime.now(ZoneInfo("Asia/Manila"))

    email_subject = f"PSE Summary - {ph_time.strftime("%Y-%m-%d %H:%M:%S")}"
    email_service.send_message(subject=email_subject
                            , message=email_content
                            , sender=EMAIL_SENDER
                            , receipient=EMAIL_RECIPIENT)

def run():
    stock_data = get_stock_data()
    send_email(stock_data)


if __name__ == "__main__":
    run()
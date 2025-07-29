import sib_api_v3_sdk
from app.models.stock_model import Stock
from app.services.stock_service import StockService
from app.config import EMAIL_API_KEY, STOCK_LIST, EMAIL_SENDER, EMAIL_RECEIPIENT
from app.services.email_service import EmailService
stock_service = StockService()

stock_data: list[Stock] = []
for code in STOCK_LIST.split(','):
    result = stock_service.get_stock_data(code)
    stock_data.append(result)



email_content = stock_service.build_email_message(stock_data)
email_service = EmailService()

email_service.send_message(subject="PSE Summary"
                           , message=email_content
                           , sender=EMAIL_SENDER
                           , receipient=EMAIL_RECEIPIENT)
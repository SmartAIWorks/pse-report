
import os
from dotenv import load_dotenv


load_dotenv()

EMAIL_API_KEY = os.getenv("EMAIL_API_KEY", '')
EMAIL_SENDER = os.getenv("EMAIL_SENDER", '')
EMAIL_RECIPIENT = os.getenv("EMAIL_RECIPIENT", '')
STOCK_LIST = os.getenv("STOCK_LIST", '')
COIN_LIST = os.getenv("COIN_LIST", '')
ASSET_AVG_PRICE = os.getenv("ASSET_AVG_PRICE", '')
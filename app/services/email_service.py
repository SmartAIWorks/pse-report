import sib_api_v3_sdk

from app.config import EMAIL_API_KEY
from app.models.stock_model import Stock



class EmailService:
    def __init__(self, api_key: str | None = None):
        key = api_key if api_key else EMAIL_API_KEY
        configuration = sib_api_v3_sdk.Configuration()
        configuration.api_key['api-key'] = key
        self.api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

    
    def send_message(self, subject: str, message: str, sender:str, receipient: str):
       
        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
            to= [{"email": receipient}],
            sender=  {"email": sender},
            subject= subject,
            html_content=message)
        
        api_response = self.api_instance.send_transac_email(send_smtp_email)
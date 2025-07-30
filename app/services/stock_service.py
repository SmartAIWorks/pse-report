import requests
from app.models.stock_model import Stock
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

        return Stock(name = name
                     , code = code
                     , price= price
                     , currency= currency
                     , percent_change= percent_change
                     , volume= volume)
    

        
    def build_email_message(self, stock_data: list[Stock]):
    
      print(stock_data)
      table_row_format =  """<tr>
          <td style="padding: 10px;">{name}</td>
          <td style="padding: 10px;">{code}</td>
          <td style="padding: 10px;">{price}</td>
          <td style="padding: 10px;">{currency}</td>
                    <td style="padding: 10px; {percent_change_style}"><b>{percent_change}%</b></td>
          <td style="padding: 10px;">{volume}</td>
          <td style="padding: 10px;">{value}</td>
        </tr>"""
      
      table_rows =  "\n".join([table_row_format.format(name= stock.name
                                                       ,code = stock.code
                                                       ,price=stock.price
                                                       ,currency=stock.currency
                                                       ,percent_change_style = "color:red"  if stock.percent_change < 0 else "color:green" if stock.percent_change > 0 else ''
                                                       ,percent_change=stock.percent_change
                                                       ,volume="{:,}".format(stock.volume)
                                                       ,value = "{:,}".format(stock.price * stock.volume)) for stock in stock_data])
      
      print(table_rows)
      return PSE_EMAIL_TEMPLATE.format(table_rows=table_rows)


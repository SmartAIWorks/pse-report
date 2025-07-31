from app.models.trading_asset import TradingAsset
from app.utils.email_helper import PSE_EMAIL_TEMPLATE

def buil_email_message(trading_assets: list[TradingAsset]):
        table_row_format =  """<tr>
          <td style="padding: 10px;">{name}</td>
          <td style="padding: 10px;">{code}</td>
          <td style="padding: 10px;">{price}</td>
          <td style="padding: 10px;">{currency}</td>
                    <td style="padding: 10px; {percent_change_style}"><b>{percent_change}%</b></td>
          <td style="padding: 10px;">{volume}</td>
          <td style="padding: 10px;">{value}</td>
        </tr>"""
      
        table_rows =  "\n".join([table_row_format.format(name= asset.name
                                                       ,code = asset.code
                                                       ,price="{:,}".format(asset.price)
                                                       ,currency=asset.currency
                                                       ,percent_change_style = "color:red"  if asset.percent_change < 0 else "color:green" if asset.percent_change > 0 else ''
                                                       ,percent_change="{:,.2f}".format(asset.percent_change)
                                                       ,volume="-" if asset.volume < 0 else "{:,}".format(asset.volume)
                                                       ,value = "{:,}".format(asset.value)) for asset in trading_assets])
      
        print(table_rows)
        return PSE_EMAIL_TEMPLATE.format(table_rows=table_rows)
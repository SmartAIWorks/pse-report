PSE_EMAIL_TEMPLATE = '''<!DOCTYPE html>
<html>
  <body style="font-family: Arial, sans-serif; margin: 0; padding: 20px; background-color: #f9f9f9;">
    <table style="width: 100%; max-width: 600px; margin: auto; background-color: #ffffff; border-collapse: collapse; border: 1px solid #ddd;">
      <thead>
        <tr style="background-color: #f0f0f0; text-align: left;">
          <th style="padding: 12px; border-bottom: 1px solid #ddd;">Name</th>
          <th style="padding: 12px; border-bottom: 1px solid #ddd;">Code</th>
          <th style="padding: 12px; border-bottom: 1px solid #ddd;">Price</th>
          <th style="padding: 12px; border-bottom: 1px solid #ddd;">Currency</th>
          <th style="padding: 12px; border-bottom: 1px solid #ddd;">% Change</th>
          <th style="padding: 12px; border-bottom: 1px solid #ddd;">Volume</th>
          <th style="padding: 12px; border-bottom: 1px solid #ddd;">Value</th>
        </tr>
      </thead>
      <tbody>
       {table_rows}
       
      </tbody>
    </table>
  </body>
</html>
'''
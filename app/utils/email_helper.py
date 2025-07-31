PSE_EMAIL_TEMPLATE = '''<!DOCTYPE html>
<html>
  <body style="font-family: 'Segoe UI', Roboto, Arial, sans-serif; margin: 0; padding: 30px; background-color: #f3fdf5;">
    
    <!-- Card Container -->
    <div style="max-width: 720px; margin: auto; background-color: #ffffff; border-radius: 12px; padding: 24px; box-shadow: 0 16px 24px rgba(46, 125, 50, 0.1);">
      
      <!-- Title -->
      <h2 style="color: #2e7d32; margin-top: 0;">📊 Trading Asset Summary</h2>
      
      <!-- Short Message -->
      <p style="font-size: 16px; color: #444; line-height: 1.5;">
        Here’s your latest trading asset summary. The table below shows the current prices, volume, value, and performance metrics for your watched assets.
        Stay informed and make data-driven decisions with confidence.
      </p>
      
      <!-- Data Table -->
      <table style="width: 100%; border-collapse: collapse; margin-top: 20px;">
        <thead>
          <tr style="background-color: #2e7d32; color: #ffffff; text-align: left;">
            <th style="padding: 12px;">Name</th>
            <th style="padding: 12px;">Code</th>
            <th style="padding: 12px;">Price</th>
            <th style="padding: 12px;">Currency</th>
            <th style="padding: 12px;">% Change</th>
            <th style="padding: 12px;">Volume</th>
            <th style="padding: 12px;">Value</th>
            <th style="padding: 12px;">Performance</th>
          </tr>
        </thead>
        <tbody>
          {table_rows}
        </tbody>
      </table>
    </div>

    <!-- Footer -->
    <p style="text-align: center; color: #6b8f71; font-size: 12px; margin-top: 30px;">
      © {year} Loanify — All rights reserved.
    </p>
  </body>
</html>

'''
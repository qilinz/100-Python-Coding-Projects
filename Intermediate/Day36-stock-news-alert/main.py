import requests
import os
import json
from datetime import datetime, timedelta
from twilio.rest import Client
import numpy as np
import html

ALPHA_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK = "TSLA"
COMPANY_NAME = "Tesla"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then check news (STEP 2)
# 1.1 get data use alpha vantage api
parameters_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.environ["ALPHA_VANTAGE_KEY"],
}

response_stock = requests.get(ALPHA_ENDPOINT, params=parameters_stock)
response_stock.raise_for_status()
data = response_stock.json()

# # save as json to check the structure
# with open("stock_data.json", "w") as file:
#     json.dump(data, file, indent=4)

# 1.2 get the date to find stock price
stock_data = data["Time Series (Daily)"]
today = datetime.now().date()
# datetime calculation. source https://stackoverflow.com/questions/441147/how-to-subtract-a-day-from-a-date
yesterday = str(today - timedelta(days=1))
two_days_before = str(today - timedelta(2))

# 1.3 calculate the change of the stock price
yesterday_close = float(stock_data[yesterday]["4. close"])
two_days_before_close = float(stock_data[two_days_before]["4. close"])
change = np.round((yesterday_close - two_days_before_close) / two_days_before_close, 2)

# trigger the news finding only when the change >= 5%
if abs(change) >= 0.05:

    ## STEP 2: Use https://newsapi.org
    # Get the first 3 news pieces for the COMPANY_NAME.
    parameters_news = {
        "qInTitle": COMPANY_NAME,
        "from": two_days_before,
        "sortBy": "publishedAt",
        "apiKey": os.environ["NEWS_KEY"],
    }

    response_news = requests.get(NEWS_ENDPOINT, params=parameters_news)
    response_news.raise_for_status()
    data = response_news.json()

    news = data["articles"][:3]

    # # save as json to check the structure
    # with open("news_data.json", "w") as file:
    #     json.dump(data, file, indent=4)

    ## STEP 3: Format the SMS message
    if change > 0:
        sms_mark = "🔺"
    else:
        sms_mark = "🔻"

    stock_info = f"\n{STOCK}: {sms_mark} {change*100}%"
    news_content = ""
    for piece in news:
        news_content += f"\nHeadline: {piece['title']}\n"
        news_content += f"Brief: {piece['description']}\n"

    news_content = html.unescape(news_content)

    ## STEP 4: Use https://www.twilio.com
    # Send a separate message with the percentage change and each article's title and description to your phone number.
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=f"{stock_info}{news_content}",
                         from_=os.environ['TWILIO_NUMBER'],
                         to='YOUR NUMBER'
                     )

    print(message.sid)
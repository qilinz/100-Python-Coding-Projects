import requests
from bs4 import BeautifulSoup
import pprint
import lxml
import smtplib
import os

# STEP 1: Find the url of the target product and define the desired price
product_url = "https://www.amazon.fr/Console-Nintendo-Switch-paire-grises/dp/B07W13KJZC/"
desired_price = 260


# STEP 2: Get the current price
# check http://myhttpheader.com for headers info
header = {
    "User-Agent": "YOUR INFO",
    "Accept-Language": "en-us",
}
response = requests.get(product_url, headers=header)
response.raise_for_status()

data = response.text

soup = BeautifulSoup(data, "html.parser")
price = soup.select_one("#priceblock_ourprice").getText()
title = soup.select_one("#productTitle").getText()
price_slice = price[:-2]
price = float(price_slice.replace(",", "."))


# STEP 3: Email user when the price meets the expectation
if price < desired_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(
            user=os.environ["GMAIL"],
            password=os.environ["GMAIL_KEY"]
        )
        connection.sendmail(
            from_addr=os.environ["GMAIL"],
            to_addrs="YOUR EMAIL",
            msg=f"Subject: Price Dropped! {title}\n\nCurrent price is {price} €. Please check {product_url}"
        )

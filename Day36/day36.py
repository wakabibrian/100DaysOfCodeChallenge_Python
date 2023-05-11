import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_PRICE_API = "EJXOEH3J2VREIOPP"
NEWS_API_KEY = "5e12146bb6ed488adbbd58556e633383"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://gnews.io/api/v4/search"

account_sid = 'AC36f1949ee8c4f9f1cc9259966ec747c1'
auth_token = "e627c7fe6489770612c1c523c6e107c0"


# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_PRICE_API
}

response = requests.get(STOCK_ENDPOINT, params=parameters)
response.raise_for_status()

stock_data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

#  Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = float(yesterday_closing_price) - \
    float(day_before_yesterday_closing_price)

up_down = None

if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_difference = round(
    (difference/float(yesterday_closing_price)) * 100)

# If percentage is greater than 5 then print("Get News").
if abs(percentage_difference) > 0.1:
    news_params = {
        "q": COMPANY_NAME,
        "apikey": NEWS_API_KEY,
    }

    response = requests.get(NEWS_ENDPOINT, news_params)
    response.raise_for_status()

    data = response.json()["articles"]
    first_three_articles = [value for value in data[:3]]

    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{percentage_difference}%\nHeadline: {article['title']}\nBrief: {article['description']}" for article in first_three_articles]
    for article in formatted_articles:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                body=article,
                from_='+12706068755',
                to='+256781876735'
            )
        print(message.status)

import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_PRICE_API = "EJXOEH3J2VREIOPP"

parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_PRICE_API
}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
response = requests.get(STOCK_ENDPOINT, params=parameters)
response.raise_for_status()

stock_data = response.json()["Time Series (Daily)"]
# print(data["Time Series (Daily)"]["2023-05-10"]["4. close"])
data_list = [value for (key, value) in stock_data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

#  Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(float(day_before_yesterday_closing_price) -
                 float(yesterday_closing_price))

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_difference = (difference/float(yesterday_closing_price)) * 100

# If percentage is greater than 5 then print("Get News").
if percentage_difference > 5:
    print("Get News")

# STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

# STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

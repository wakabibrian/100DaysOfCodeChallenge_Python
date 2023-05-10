# --- What is API Authentication and Why Do We Need to Authenticate Ourselves? --- #
# Authenticate ourselves so that we are more secure as we get data from API providers
# Some APIs require authentication
# Previously, they were free APIs. Some APIs can have a paid tier for commercial and fancy applications
# Some people sell APIs because of the costs involved
# Through API Key (personal account), the providers can track how much you are using their data
# hence authorise or denie access

# --- Using API Keys to Authenticate and Get the Weather from OpenWeatherMap ---#
# --- Challenge - Check if it Will Rain in the Nextx 12 Hours ---#
# --- Sending SMS via the Twilio API ---#

import requests
from twilio.rest import Client

account_sid = 'AC36f1949ee8c4f9f1cc9259966ec747c1'
auth_token = '7eae89d9db81f95f728dafd1247e6920'

api_key = "69f04e4613056b159c2761a9d9e664d2"
# MY_LAT = 0.3747545
# MY_LONG = 32.5572151
MY_LAT = 23.731939
MY_LONG = -99.150818

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(
    "https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

weather_data = response.json()

weather_slice = weather_data["hourly"][:12]
condition_codes = [hour_data["weather"][0]["id"]
                   for hour_data in weather_slice]

if any(condition_codes) < 700:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an umbrella",
            from_='+12706068755',
            to='+256781876735'
        )
    print(message.status)

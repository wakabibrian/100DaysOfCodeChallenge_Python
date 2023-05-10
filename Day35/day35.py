# --- What is API Authentication and Why Do We Need to Authenticate Ourselves? --- #
# Authenticate ourselves so that we are more secure as we get data from API providers
# Some APIs require authentication
# Previously, they were free APIs. Some APIs can have a paid tier for commercial and fancy applications
# Some people sell APIs because of the costs involved
# Through API Key (personal account), the providers can track how much you are using their data
# hence authorise or denie access

# --- Using API Keys to Authenticate and Get the Weather from OpenWeatherMap ---#
# --- Challenge - Check if it Will Rain in the Nextx 12 Hours ---#

import requests

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
    print("Bring an Umbrella")

# will_rain = False

# for condition_code in condition_codes:
#     if condition_code < 700:
#         will_rain = True

# if will_rain:
#     print("Bring an Umbrella")

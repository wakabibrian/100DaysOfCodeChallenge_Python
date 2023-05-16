import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/dad72c5769ebd68b690a01022338ff46/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

# 5. In main.py check if sheet_data contains any values for the "iataCode" key.
# If not, then the IATA Codes column is empty in the Google Sheet.
# In this case, pass each city name in sheet_data one-by-one to the FlightSearch class.
# For now, the FlightSearch class can respond with "TESTING" instead of a real IATA code.
# You should use the response from the FlightSearch class to update the sheet_data dictionary.
# Print the updated sheet_data dictionary and you should see:

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

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

#     6. In the DataManager Class make a PUT request and use the row id
# from sheet_data to update the Google Sheet with the IATA codes. (Do this using code).
# HINT: Remember to check the checkbox to allow PUT requests in Sheety.

# Take a look at the Sheety API documentation to help you:

from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
sheety_data = data_manager.get_destination_data()

# 5. In main.py check if sheet_data contains any values for the "iataCode" key.
# If not, then the IATA Codes column is empty in the Google Sheet.
# In this case, pass each city name in sheet_data one-by-one to the FlightSearch class.
# For now, the FlightSearch class can respond with "TESTING" instead of a real IATA code.
# You should use the response from the FlightSearch class to update the sheet_data dictionary.
# Print the updated sheet_data dictionary and you should see:
# for row in sheety_data:
#     if row["iataCode"] == "":
#         data_manager.update_destination_codes()

# print(sheety_data)

if sheety_data[0]["iataCode"] == "":
    flight_search = FlightSearch()
    for row in sheety_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheety_data}")

    data_manager.destination_data = sheety_data
    data_manager.update_destination_codes()

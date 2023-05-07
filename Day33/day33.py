# ----------------What are Application Programming Interfaces (APIs)?--------------------#
# An Application Programming Interface is a set of commands, functions, protocols and objects
# that programmers can use to create software or interact with an external system
# Through API, you use your program to make a Request to an external system for some piece of data
# Then the external system will Respond to you appropriately and give the datas

# ----------------API Endpoints and Making API Calls--------------------#
# An API Endpoint is one of the most important aspect of an API
# You can imagine it as a location; location the data is stored
# An API Endpoint is simply a URL (location where the data you want can be found)
# You also have to make a request over the internet (API request) - requesting data from the endpoint
# API request - simply requesting/getting a piece of data using their API
import requests

# url takes the endpoint
# returns a response code
response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)

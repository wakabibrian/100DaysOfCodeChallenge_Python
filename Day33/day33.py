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

# ------Working with Responses: HTTP Codes, Exceptions & JSON Data--------#
# Response tells us if our request succeeded or it failed
# 404 response code means that the thing doesnt exist
# Always look at the first number
# 1XX - hold on, something is happening - This is not final
# 2XX - Everything was successful - you can get the data
# 3XX - Go Away (You dont have permission to get this thing)
# 4XX - You screwed Up e.g 404 - you screwed up, the thing you are looking for doesnt exist
# 5XX - I (server for the data) screwed up; may be server or website is down

# # actual response status code instead of response object
# print(response.status_code)
response.raise_for_status()  # incase of an error in the API

# data = response.json()
data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)
print(iss_position)

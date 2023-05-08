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
# import requests

# # url takes the endpoint
# # returns a response code
# response = requests.get(url="http://api.open-notify.org/iss-now.json")

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
# response.raise_for_status()  # incase of an error in the API

# # data = response.json()
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)

# ------Challenge - Build a Kanye Quotes App using the Kanye Rest API--------#
# from tkinter import *
# import requests


# def get_quote():
#     response = requests.get("https://api.kanye.rest/")
#     response.raise_for_status()

#     data = response.json()
#     quote = data["quote"]
#     canvas.itemconfig(quote_text, text=quote)


# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)

# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=(
#     "Arial", 22, "bold"), fill="white")
# canvas.grid(row=0, column=0)

# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)


# window.mainloop()

# ------Understand API Parameters: Match Sunset Times with the Current Time--------#
# API Parameters: This is a way that allows to give an input when making your API requests so
# that you can get different pieces of data back depending on your input.
# Not all APIs have parameters
# Some parameters are required and some are optional. The optional ones have default values
# from datetime import datetime
# import requests
# import datetime

# MY_LAT = 0.3747545
# MY_LONG = 32.5572151

# parameters = {
#     "lat": MY_LAT,
#     "lng": MY_LONG,
#     "formatted": 0
# }

# response = requests.get(
#     "https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()

# data = response.json()
# sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
# sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
# print(sunrise)
# print(sunset)

# time_now = datetime.datetime.now()
# hour = time_now.hour
# print(hour)

# ------Day 33 Project: ISS Overhead Notifier Project--------#
import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "wakabibrian24@gmail.com"
PASSWORD = "drduuhmbpunqudeo"
MY_LAT = 0.3747545
MY_LONG = 32.5572151


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5):
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="wakabibrian95@gmail.com",
                msg=f"Subject: Look up\n\nThe ISS is above you in the sky."
            )

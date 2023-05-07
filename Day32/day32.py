# ------------How to Send Emails with Python using SMTP--------------#
# SMTP - Simple Mail Transfer Protocol
# Email passes through the SMTP from sender email server (e.g wakabi@gmail.com - Gmail Mail Server)
# to recipient email server (e.g angella@yahoo.com - Yahoo Email Server) to recipient's computer.
# The recipient computer gets from the recipient email server (e.g Yahoo Email Server)

# Python smtplib allows us to send emails to any address on the internet

# import smtplib

# my_email = "wakabibrian23@gmail.com"
# password = "zdbjynhcskeypjfi"

# with smtplib.SMTP("smtp.gmail.com") as connection:  # Connecting to the email server
#     # TLS - Transport Layers Security; A way of securing our connection to our email server
#     # Encrypts the email for other people not to read it
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="wakabibrian23@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of my email"
#     )

# ------------Working with the datetime Module--------------#
# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# day = now.weekday()
# month = now.month

# date_of_birth = dt.datetime(year=1990, month=2, day=19, hour=4)
# print(date_of_birth)

# ------------Challenge 1 - Send Motivational Quotes on Mondays via Email--------------#
import smtplib
import datetime as dt
import random

MY_EMAIL = "wakabibrian24@gmail.com"
PASSWORD = "drduuhmbpunqudeo"


with open("quotes.txt") as quotes_file:
    quotes = quotes_file.readlines()
    random_quote = random.choice(quotes)

now = dt.datetime.now()
day = now.weekday()
if day == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="wakabibrian95@gmail.com",
            msg=f"Subject: Monday Motivation\n\n{random_quote}"
        )

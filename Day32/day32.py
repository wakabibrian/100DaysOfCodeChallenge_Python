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
# import smtplib
# import datetime as dt
# import random

# MY_EMAIL = "wakabibrian24@gmail.com"
# PASSWORD = "drduuhmbpunqudeo"


# with open("quotes.txt") as quotes_file:
#     quotes = quotes_file.readlines()
#     random_quote = random.choice(quotes)

# now = dt.datetime.now()
# day = now.weekday()
# if day == 0:
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=MY_EMAIL, password=PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs="wakabibrian95@gmail.com",
#             msg=f"Subject: Monday Motivation\n\n{random_quote}"
#         )

# ------------Day 32 Project: Automated Birthday Wisher.--------------#
# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes. e.g.
# name,email,year,month,day
# YourName,your_own@email.com,today_year,today_month,today_day

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)

# HINT 2: Use pandas to read the birthdays.csv

# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
# Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
# e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
# Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

# HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter.
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.

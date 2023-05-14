import os
import smtplib
import datetime as dt
import random
import json

MY_EMAIL = "wakabibrian24@gmail.com"
PASSWORD = os.environ.get("MY_PASSWORD")
CHALLENGE = f"- Code 10 hours\n- No to distractions\n- No eating out\n- No spending"
GOAL = f"- Finish Python and Django\n- Finish HTML, CSS, SASS\n- Finish Javascript and React\n- Finish DevOps"
PROJECTS = f"- Launch Personal Blog\n- To Do App"
REWARDS = f"- Move to a new house\n- Buy a new fridge\n- Buy a 62 inch TV"
print("Testing")

with open("quotes.txt") as quotes_file:
    quotes = quotes_file.readlines()
    random_quote = random.choice(quotes)

now = dt.datetime.now()
day = now.weekday()
if day == 0 or day == 2 or day == 3 or day == 4 or day == 5 or day == 6:
    with open("data.json", "r") as days_file:
        data = json.load(days_file)

    count_down = data["days_remaining"]

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="wakabibrian95@gmail.com",
            msg=f"Subject: Motivation and Challenge\n\nToday's Quote({now.day}/{now.month}/{now.year}):\n{random_quote}\n\nREMEMBER - The 90 Day Challenge: {count_down} Days to go:\n{CHALLENGE}\n\nGoal:\n{GOAL}\n\nProjects:\n{PROJECTS}\n\nRewards:\n{REWARDS}"
        )

    count_down -= 1
    new_data = {
        "days_remaining": count_down
    }

    data.update(new_data)
    with open("data.json", "w") as days_file:
        json.dump(data, days_file, indent=4)

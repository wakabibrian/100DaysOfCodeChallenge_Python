import requests
from datetime import datetime

APP_ID = "2ff64d50"
API_KEY = "8c97dd43ab1488c119a124ae6ab26f1c"
MY_EMAIL = "wakabibrian95@gmail.com"

GENDER = "male"
WEIGHT = 58
HEIGHT = 182.88
AGE = 33

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercise  you did: ")

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(exercise_endpoint,
                         json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%y")
today_time = datetime.now().strftime("%H:%M:%S")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workouts": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    print(sheet_inputs)

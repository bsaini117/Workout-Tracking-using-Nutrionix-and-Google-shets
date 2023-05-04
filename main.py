import requests
from datetime import datetime
import os

today = datetime.now()
today_formatted = today.strftime("%x")
time_formatted = today.strftime("%X")


API_KEY = "ba46ca79364f7d18eacda0208d27c404"
API_ID = "e8a09bd0"

sheety_endpoint = "https://api.sheety.co/a5b9f38df3cc01445d54b5e990cb5e1d/workoutTracking/workouts"
sheety_token = "k1!6iH4pmOto"


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

auth_header_nutrix = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}


exercise_config = {
    "query": input("Tell me which exercise you did: ")
}

response = requests.post(url=exercise_endpoint, json=exercise_config, headers=auth_header_nutrix)
response.raise_for_status()
data = response.json()

exercise_data = data["exercises"][0]


auth_header_sheety = {"Authorization": f"Bearer {sheety_token}"}
params = {
    "workout":{
        "date": today_formatted,
        "time": time_formatted,
        "exercise": exercise_data["name"].title(),
        "duration": exercise_data["duration_min"],
        "calories": exercise_data["nf_calories"]

    }
}
sheety_reponse = requests.post(url=sheety_endpoint, json=params, headers=auth_header_sheety)
print(sheety_reponse.text)

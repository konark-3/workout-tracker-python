import requests
from datetime import datetime
import os

# Ran 2 miles and walked for 3Km.

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get('API_KEY')

today = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%X")

user = input("Tell me which exercise you did today? ")

endpoint1 = 'https://trackapi.nutritionix.com/v2/natural/exercise'
endpoint2 = 'https://api.sheety.co/2f779484d018b7c24ec45f10323a5ca1/myWorkouts/workouts'


exercise_params = {
    'query': user
}

exercise_headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

response1 = requests.post(endpoint1, json=exercise_params, headers=exercise_headers)
response1.raise_for_status()

data = response1.json()


exercise = None
duration_min = None
nf_calories = None

headers = {
    "Authorization": "Basic tyt#####"
}

for number in range(0, len(data['exercises'])):
    exercise = data['exercises'][number]['name'].title()
    duration_min = data['exercises'][number]['duration_min']
    nf_calories = data['exercises'][number]['nf_calories']

    add_params = {
        "workout": {
            "date": today,
            "time": time_now,
            "exercise": exercise,
            "duration": duration_min,
            "calories": nf_calories
        }
    }
    response2 = requests.post(url=endpoint2, json=add_params, headers=headers)
    response2.raise_for_status()
    print(response2.text)

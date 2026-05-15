import requests
from datetime import datetime

API_KEY = "05f995fc64c4b6bd275fec64aafb65de"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def fetch_weather(city):

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)

        print("STATUS:", response.status_code)
        print("DATA:", response.text)

        response.raise_for_status()

        data = response.json()

        weather_data = {
            "City": city,
            "Temperature": data["main"]["temp"],
            "Humidity": data["main"]["humidity"],
            "Wind Speed": data["wind"]["speed"],
            "Weather": data["weather"][0]["main"],
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        return weather_data

    except Exception as e:
        print("ERROR:", e)
        return None
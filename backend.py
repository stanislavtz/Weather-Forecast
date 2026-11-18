import truststore
truststore.inject_into_ssl()

import os
import requests
from dotenv import load_dotenv
from geopy.geocoders import Nominatim

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")


def get_weather_data(place, days):
    geolocator = Nominatim(user_agent="weather_forecast")

    location = geolocator.geocode(place)
    lat = location.latitude
    lon = location.longitude

    weather_url = (f"https://data.api.xweather.com/forecasts/{lat}%2C{lon}?"
                   f"from=now&to={days}&plimit={days}&"
                   f"client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}")
    response = requests.get(weather_url)
    data = response.json()

    arr = data["response"][0]["periods"]

    dates = [d["dateTimeISO"] for d in arr]
    temperatures = [t["avgTempC"] for t in arr]
    weathers = [(w["dateTimeISO"], w["weather"]) for w in arr]

    return dates, temperatures, weathers

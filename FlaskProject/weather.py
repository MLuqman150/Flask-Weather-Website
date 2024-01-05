import os
import requests
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()	

def getCurrentWeather(city="Lahore"):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print("\n******** Get Current Weather ********\n")

    city = input("Enter city name: ")
# check for empty string 
    if not bool(city.strip()):
        city = "Bahawalpur"

    weather_data = getCurrentWeather(city)
    
    print("\n******** Weather Data ********\n")
    pprint(weather_data)
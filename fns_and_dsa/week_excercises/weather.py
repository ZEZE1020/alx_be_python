import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def get_weather(city_name):
    api_key = os.getenv('API_KEY')
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city_name}"
    
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        description = weather["description"]
        
        print(f"Temperature: {temperature}K")
        print(f"Pressure: {pressure}hPa")
        print(f"Humidity: {humidity}%")
        print(f"Weather description: {description}")
    else:
        print("City Not Found")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)

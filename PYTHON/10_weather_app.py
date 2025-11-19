# Weather app

import requests

def weather_app():
    city = input("Enter a city name : ")
    url = "https://api.openweathermap.org/data/2.5/weather_app"
    api_key = "1fb82a7497e397dfb1fbaca330716736"
    
    params = {
        "q" : city,
        "appid" : api_key,
        "units" : "metric"
    }
    
    try:
        response = requests.get(url, params)
        data = response.json()
        print("Weather in ", city)
        print("Temperature : ", data["temp"])
        print("Humidity : ", data["humidity"])
        print("Weather description :" , data["description"])               
        
    except requests.exceptions.RequestException as e:
        print("Error ", e)
        
        
# Run the app
weather_app()
    
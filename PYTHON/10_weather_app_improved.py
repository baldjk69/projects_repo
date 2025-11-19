# Weather app

import requests

def weather_app():
    city = input("Enter a city name : ").strip()
    url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = "1fb82a7497e397dfb1fbaca330716736"
    
    params = {
        "q" : city,
        "appid" : api_key,
        "units" : "metric"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status() # Handle errors (e.g. invalid city)
        data = response.json()
        
        # Extract weather details
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        
        print(f"\n Weather in {city.capitalize()}")
        print(f"Temperature : {temperature} °C")
        print(f"Humidity : {humidity}%")
        print(f"Weather description : {description.capitalize()}")               
        
    except requests.exceptions.HTTPError:
        print("City not found. Please check the name and try again.")
    
    except requests.exceptions.RequestException as e:
        print("Network or API error:", e)
        
        
# Run the app
weather_app() 





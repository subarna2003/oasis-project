import requests

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] != 200:
        print("Error:", data["message"])
        return None
    return data

def main():
    api_key = "YOUR_API_KEY"
    location = input("Enter city name or ZIP code: ")
    
    weather_data = get_weather(api_key, location)
    if weather_data:
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        weather = weather_data["weather"][0]["description"]
        
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather}")

if __name__ == "__main__":
    main()

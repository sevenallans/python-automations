import sys
import json
import urllib.request
import urllib.parse

def get_weather(city):
    url = f"https://wttr.in/{urllib.parse.quote(city)}?format=j1"
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            current_condition = data['current_condition'][0]
            temp_c = current_condition['temp_C']
            temp_f = current_condition['temp_F']
            weather_desc = current_condition['weatherDesc'][0]['value']
            
            print(f"\n--- Weather Report for {city.title()} ---")
            print(f"Condition:   {weather_desc}")
            print(f"Temperature: {temp_c}°C / {temp_f}°F")
            print(f"Feels Like:  {current_condition['FeelsLikeC']}°C / {current_condition['FeelsLikeF']}°F")
            print(f"Humidity:    {current_condition['humidity']}%")
            print(f"Wind Speed:  {current_condition['windspeedKmph']} km/h")
    except Exception as e:
        print(f"Error fetching weather data for '{city}': {e}")

def main():
    if len(sys.argv) > 1:
        city = " ".join(sys.argv[1:])
    else:
        city = input("Enter city name: ").strip()
    
    if not city:
        city = "London"
        print("No city provided, defaulting to London.")
        
    get_weather(city)

if __name__ == "__main__":
    main()

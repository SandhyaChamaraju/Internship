import requests

API_KEY = "YOUR_OPENWEATHER_API_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print("Error:", response.json().get("message", "Unable to fetch weather"))
        return

    data = response.json()

    print("\n" + "=" * 40)
    print(f"Weather in {data['name']}, {data['sys']['country']}")
    print("=" * 40)
    print(f"Temperature : {data['main']['temp']:.1f} °C")
    print(f"Feels Like  : {data['main']['feels_like']:.1f} °C")
    print(f"Condition   : {data['weather'][0]['description'].title()}")
    print(f"Humidity    : {data['main']['humidity']}%")
    print(f"Wind Speed  : {data['wind']['speed']} m/s")
    print(f"Pressure    : {data['main']['pressure']} hPa")
    print(f"Visibility  : {data.get('visibility', 0) / 1000:.1f} km")
    print("=" * 40)


while True:
    city = input("\nEnter city name (or 'quit' to exit): ").strip()

    if city.lower() == "quit":
        print("Goodbye!")
        break

    if city:
        get_weather(city)

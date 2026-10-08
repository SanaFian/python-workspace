"""
Project 06: Mini Weather App
Fetches real-time weather data using a public REST API and parses JSON response.
"""

import urllib.request
import json

# Predefined coordinates for selected major cities
CITIES = {
    "Tehran": {"lat": 35.6892, "lon": 51.3890},
    "London": {"lat": 51.5074, "lon": -0.1278},
    "Tokyo": {"lat": 35.6762, "lon": 139.6503},
    "New York": {"lat": 40.7128, "lon": -74.0060},
}


def fetch_weather(city_name: str, lat: float, lon: float) -> None:
    """Fetches and displays current weather data for given coordinates."""
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    try:
        print(f"\nFetching weather details for {city_name}...")
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                data = json.loads(response.read().decode("utf-8"))
                current = data.get("current_weather", {})

                temperature = current.get("temperature")
                wind_speed = current.get("windspeed")
                time_fetched = current.get("time")

                print("=" * 35)
                print(f"📍 City: {city_name}")
                print(f"🌡️  Temperature: {temperature}°C")
                print(f"💨 Wind Speed: {wind_speed} km/h")
                print(f"🕒 Recorded Time: {time_fetched}")
                print("=" * 35)
            else:
                print(f"Failed to fetch data. HTTP Status: {response.status}")

    except Exception as error:
        print(f"Network or data parsing error: {error}")


def main():
    while True:
        print("\n--- Mini Weather Reporter ---")
        print("Available cities:")
        for idx, city in enumerate(CITIES.keys(), start=1):
            print(f"[{idx}] {city}")
        print("[0] Exit")

        choice = input("\nSelect a city (number): ").strip()

        if choice == "0":
            print("Exiting weather app. Goodbye!")
            break

        city_names = list(CITIES.keys())
        if choice.isdigit() and 1 <= int(choice) <= len(city_names):
            selected_city = city_names[int(choice) - 1]
            coords = CITIES[selected_city]
            fetch_weather(selected_city, coords["lat"], coords["lon"])
        else:
            print("Invalid selection! Please enter a valid number.")


if __name__ == "__main__":
    main()

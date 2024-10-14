import json
import os

import weather


def initialise_config(path: str) -> dict:
    try:
        with open(path, "r") as f:
            config = json.loads(f.read())
    except Exception as e:
        print(f"Unable to initialize project {e}")
        exit(1)
    return config



if __name__ == '__main__':
    config = initialise_config("config.json")
    key = os.environ['weather_api_key']
    if key is None:
        print("Error: API key is not set in environment variables.")
        exit(1)
    weather_dict = weather.get_current_weather(url=config['url'],key=key, city="Bucharest")
    print(json.dumps(weather_dict, indent=4))

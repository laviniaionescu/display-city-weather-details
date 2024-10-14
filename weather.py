import json

import requests


def get_current_weather(url: str, key: str, city: str = "Bucharest"):
    try:
        response = requests.get(url + city, headers={"key": "6d49887f810d4bf0aa1165040240304"})
        if response.status_code == 200:
            weather_dict = json.loads(response.text)
            if weather_dict.get('error'):
                raise Exception("City does not exist in our database")
            return weather_dict
        else:
            raise Exception(f"Something went wrong with the API\n"
                            f"Code: {response.status_code}\n"
                            f"Message: {response.text}")
    except Exception as e:
        print(e)
import requests


def forecast_air_pollution(lat: str, lon: str, api_key: str = '2a045ada80a040c4d68880e3abc55c5f'):
    """
    "Get the balance of an bitcoin address"

    """
    url = f"https://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={lat}&lon={lon}&appid={api_key}"
    print("URL:", url)
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation


def current_air_pollution(lat: str, lon: str, api_key: str = '2a045ada80a040c4d68880e3abc55c5f'):
    """
    "Get the balance of an bitcoin address"

    """
    url = f"https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"
    print("URL:", url)
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

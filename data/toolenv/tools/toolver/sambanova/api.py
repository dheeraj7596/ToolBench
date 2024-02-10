import requests


def forecast_air_pollution(lat: str, lon: str, api_key: str = '2a045ada80a040c4d68880e3abc55c5f'):
    """
    "Get the balance of an bitcoin address"

    """
    url = f"https://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={lat}&lon={lon}&appid={api_key}"
    print("TOOL: Forecast Air Pollution")
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
    print("TOOL: Current Air Pollution")
    print("URL:", url)
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation


def geographical_coordinates(q, limit, api_key: str = '2a045ada80a040c4d68880e3abc55c5f'):
    """
    "Get the balance of an bitcoin address"

    """
    q = "+".split(q.strip().split(" "))
    url = f"https://api.openweathermap.org/geo/1.0/direct?q={q}&limit={limit}&appid={api_key}"
    print("TOOL: Geographical Coordinates")
    print("URL:", url)
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation


def current_weather_city(q, units, mode, lang, api_key: str = '2a045ada80a040c4d68880e3abc55c5f'):
    """
    "Get the balance of an bitcoin address"

    """
    if units is None or units == "None":
        units = "standard"
    else:
        units = units.lower()

    if mode is None or mode == "None":
        mode = "json"
    else:
        mode = mode.lower()

    if lang is None or lang == "None":
        lang = "en"
    else:
        lang = lang.lower()

    q = "+".split(q.strip().split(" "))
    url = f"https://api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}&units={units}&mode={mode}&lang={lang}"
    print("TOOL: Current Weather City")
    print("URL:", url)
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation


def forecast_weather_city(q, units, mode, lang, api_key: str = '2a045ada80a040c4d68880e3abc55c5f'):
    """
    "Get the balance of an bitcoin address"

    """
    if units is None or units == "None":
        units = "standard"
    else:
        units = units.lower()

    if mode is None or mode == "None":
        mode = "json"
    else:
        mode = mode.lower()

    if lang is None or lang == "None":
        lang = "en"
    else:
        lang = lang.lower()

    q = "+".split(q.strip().split(" "))
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={q}&appid={api_key}&units={units}&mode={mode}&lang={lang}"
    print("TOOL: Forecast Weather City")
    print("URL:", url)
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation


def forecast_weather_latitude_longitude(lat, lon, units, mode, lang, api_key: str = '2a045ada80a040c4d68880e3abc55c5f'):
    """
    "Get the balance of an bitcoin address"

    """
    if units is None or units == "None":
        units = "standard"
    else:
        units = units.lower()

    if mode is None or mode == "None":
        mode = "json"
    else:
        mode = mode.lower()

    if lang is None or lang == "None":
        lang = "en"
    else:
        lang = lang.lower()

    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units={units}&mode={mode}&lang={lang}"
    print("TOOL: Forecast Weather Latitude Longitude")
    print("URL:", url)
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation


def current_weather_latitude_longitude(lat, lon, units, mode, lang, api_key: str = '2a045ada80a040c4d68880e3abc55c5f'):
    """
    "Get the balance of an bitcoin address"

    """
    if units is None or units == "None":
        units = "standard"
    else:
        units = units.lower()

    if mode is None or mode == "None":
        mode = "json"
    else:
        mode = mode.lower()

    if lang is None or lang == "None":
        lang = "en"
    else:
        lang = lang.lower()

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units={units}&mode={mode}&lang={lang}"
    print("TOOL: Current Weather Latitude Longitude")
    print("URL:", url)
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation


def forecast_weather_zipcode(zip, units, mode, lang, api_key: str = '2a045ada80a040c4d68880e3abc55c5f'):
    """
    "Get the balance of an bitcoin address"

    """
    if units is None or units == "None":
        units = "standard"
    else:
        units = units.lower()

    if mode is None or mode == "None":
        mode = "json"
    else:
        mode = mode.lower()

    if lang is None or lang == "None":
        lang = "en"
    else:
        lang = lang.lower()

    url = f"https://api.openweathermap.org/data/2.5/forecast?zip={zip}&appid={api_key}&units={units}&mode={mode}&lang={lang}"
    print("TOOL: Forecast Weather Zipcode")
    print("URL:", url)
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation


def current_weather_zipcode(zip, units, mode, lang, api_key: str = '2a045ada80a040c4d68880e3abc55c5f'):
    """
    "Get the balance of an bitcoin address"

    """
    if units is None or units == "None":
        units = "standard"
    else:
        units = units.lower()

    if mode is None or mode == "None":
        mode = "json"
    else:
        mode = mode.lower()

    if lang is None or lang == "None":
        lang = "en"
    else:
        lang = lang.lower()

    url = f"https://api.openweathermap.org/data/2.5/weather?zip={zip}&appid={api_key}&units={units}&mode={mode}&lang={lang}"
    print("TOOL: Current Weather Zipcode")
    print("URL:", url)
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation


def delete_image_from_favorites(image_id,
                                api_key: str = 'live_r4Ir3NmMzUvp2ODgP3mfEE7kBN80gGa1JruKE7fYIeyXu97OASmseqabSUMrf2gT'):
    """
    "Get the balance of an bitcoin address"

    """
    url = f"https://api.thecatapi.com/v1/favourites/{image_id}"
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key
    }
    print("TOOL: Delete image from favorites")
    print("URL:", url)

    response = requests.get(url, headers=headers)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

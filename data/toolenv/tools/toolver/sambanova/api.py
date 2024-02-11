import requests


def forecast_air_pollution(lat: str, lon: str, api_key: str = '2a045ada80a040c4d68880e3abc55c5f'):
    """
    "Get the balance of an bitcoin address"

    """
    url = f"https://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={lat}&lon={lon}&appid={api_key}"
    print("TOOL: Forecast Air Pollution")
    print("API:", url)
    print("###")
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
    print("API:", url)
    print("###")
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
    print("API:", url)
    print("###")
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
    print("API:", url)
    print("###")
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
    print("API:", url)
    print("###")
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
    print("API:", url)
    print("###")
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
    print("API:", url)
    print("###")
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
    print("API:", url)
    print("###")
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
    print("API:", url)
    print("###")
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
    print("API:", url)
    print("###")
    response = requests.delete(url, headers=headers)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation


def find_images(size, mime_types, order, limit, breeds,
                api_key: str = 'live_r4Ir3NmMzUvp2ODgP3mfEE7kBN80gGa1JruKE7fYIeyXu97OASmseqabSUMrf2gT'):
    """
    "Get the balance of an bitcoin address"

    """
    if size is None or size == "None":
        size = "med"
    else:
        size = size.lower()

    if mime_types is None or mime_types == "None":
        mime_types = "jpg,gif,png"
    else:
        mime_types = mime_types.lower()

    if order is None or order == "None":
        order = "RANDOM"

    if limit is None or limit == "None":
        limit = "1"
    else:
        limit = str(limit)

    if breeds is None or breeds == "None":
        breeds = ""
    else:
        breeds = breeds.lower()

    url = f"https://api.thecatapi.com/v1/images/search?&size={size}&mime_types={mime_types}&order={order}&limit={limit}&breeds={breeds}'"
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key
    }
    print("TOOL: Find images")
    print("API:", url)
    print("###")
    response = requests.get(url, headers=headers)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation


def get_favorite_cat_images(api_key: str = 'live_r4Ir3NmMzUvp2ODgP3mfEE7kBN80gGa1JruKE7fYIeyXu97OASmseqabSUMrf2gT'):
    """
    "Get the balance of an bitcoin address"

    """
    url = f"https://api.thecatapi.com/v1/favourites"
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key
    }
    print("TOOL: Get favorite cat images")
    print("API:", url)
    print("###")
    response = requests.get(url, headers=headers)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation


def post_to_favorites(image_id, api_key: str = 'live_r4Ir3NmMzUvp2ODgP3mfEE7kBN80gGa1JruKE7fYIeyXu97OASmseqabSUMrf2gT'):
    """
    "Get the balance of an bitcoin address"

    """
    url = f"https://api.thecatapi.com/v1/favourites"
    querystring = {'image_id': image_id}
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key
    }
    dump_url = f"""curl -X POST 'https://api.thecatapi.com/v1/favourites' --data '{"image_id":{image_id}}'"""
    print("TOOL: Post to favorites")
    print("API:", dump_url)
    print("###")
    response = requests.post(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation


def vote_down(image_id, api_key: str = 'live_r4Ir3NmMzUvp2ODgP3mfEE7kBN80gGa1JruKE7fYIeyXu97OASmseqabSUMrf2gT'):
    """
    "Get the balance of an bitcoin address"

    """
    url = f"https://api.thecatapi.com/v1/votes"
    querystring = {'image_id': image_id, "value": -1}
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key
    }
    dump_url = f"""curl -X POST 'https://api.thecatapi.com/v1/votes' --data '{"image_id":{image_id}, "value":-1}'"""
    print("TOOL: Vote down")
    print("API:", dump_url)
    print("###")
    response = requests.post(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation


def vote_up(image_id, api_key: str = 'live_r4Ir3NmMzUvp2ODgP3mfEE7kBN80gGa1JruKE7fYIeyXu97OASmseqabSUMrf2gT'):
    """
    "Get the balance of an bitcoin address"

    """
    url = f"https://api.thecatapi.com/v1/votes"
    querystring = {'image_id': image_id, "value": 1}
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key
    }
    dump_url = f"""curl -X POST 'https://api.thecatapi.com/v1/votes' --data '{"image_id":{image_id}, "value":1}'"""
    print("TOOL: Vote up")
    print("API:", dump_url)
    print("###")
    response = requests.post(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation


def booking(booking_type, means_of_transportation="None", location_from="None", location_to="None",
            min_price_ticket="None", max_price_ticket="None", num_adults="None", num_children="None",
            departure_date="None", return_date="None", location="None", checkin_date="None", checkout_date="None",
            num_rooms="None", room_type="None", min_price_room="None", max_price_room="None"):
    if departure_date == "None":
        departure_date_str = """API.set_departure_date("None")"""
    else:
        departure_date_str = f"""departure_date = Date({departure_date})
API.set_departure_date(departure_date)"""
    if return_date == "None":
        return_date_str = """API.set_return_date("None")"""
    else:
        return_date_str = f"""return_date = Date({return_date})
API.set_return_date(return_date)"""

    if checkin_date == "None":
        checkin_date_str = """API.set_checkin_date("None")"""
    else:
        checkin_date_str = f"""checkin_date = Date({checkin_date})
API.set_checkin_date(checkin_date)"""

    if checkout_date == "None":
        checkout_date_str = """API.set_checkout_date("None")"""
    else:
        checkout_date_str = f"""checkout_date = Date({checkout_date})
API.set_checkout_date(checkout_date)"""

    if min_price_ticket == "None":
        min_price_ticket_str =  f"""API.set_min_ticket_price("None")"""
    else:
        min_price_ticket_str = f"""API.set_min_ticket_price({min_price_ticket})"""

    if max_price_ticket == "None":
        max_price_ticket_str =  f"""API.set_max_ticket_price("None")"""
    else:
        max_price_ticket_str = f"""API.set_max_ticket_price({max_price_ticket})"""

    if num_adults == "None":
        num_adults_str =  f"""API.set_num_adults("None")"""
    else:
        num_adults_str = f"""API.set_num_adults({num_adults})"""

    if num_children == "None":
        num_children_str =  f"""API.set_num_children("None")"""
    else:
        num_children_str = f"""API.set_num_children({num_children})"""

    if num_rooms == "None":
        num_rooms_str =  f"""API.set_num_rooms("None")"""
    else:
        num_rooms_str = f"""API.set_num_rooms({num_rooms})"""

    if min_price_room == "None":
        min_price_room_str =  f"""API.set_min_room_price("None")"""
    else:
        min_price_room_str = f"""API.set_min_room_price({min_price_room})"""

    if max_price_room == "None":
        max_price_room_str =  f"""API.set_max_room_price("None")"""
    else:
        max_price_room_str = f"""API.set_max_room_price({max_price_room})"""

    t = f"""API.select_booking_type(\"{booking_type}\")
API.select_transportation(\"{means_of_transportation}\")
location_from = Loc(\"{location_from}\")
API.set_origin(location_from)
location_to = Loc(\"{location_to}\")
API.set_destination(location_to)
{min_price_ticket_str}
{max_price_ticket_str}
{num_adults_str}
{num_children_str}
{departure_date_str}
{return_date_str}
hotel_location = Loc({location})
API.set_hotel_location(hotel_location)
{checkin_date_str}
{checkout_date_str}
{num_rooms_str}
API.select_room_type({room_type})
{min_price_room_str}
{max_price_room_str}
API.search()"""
    print("API:", t)
    print("###")
    return "Booking done"


# def home_search(location="None", means_of_transportation="None", location_from="None", location_to="None",
#             min_price_ticket="None", max_price_ticket="None", num_adults="None", num_children="None",
#             departure_date="None", return_date="None", location="None", checkin_date="None", checkout_date="None",
#             num_rooms="None", room_type="None", min_price_room="None", max_price_room="None"):
#     if departure_date == "None":
#         departure_date_str = """API.set_departure_date("None")"""
#     else:
#         departure_date_str = f"""departure_date = Date({departure_date})
# API.set_departure_date(departure_date)"""
#     if return_date == "None":
#         return_date_str = """API.set_return_date("None")"""
#     else:
#         return_date_str = f"""return_date = Date({return_date})
# API.set_return_date(return_date)"""
#
#     if checkin_date == "None":
#         checkin_date_str = """API.set_checkin_date("None")"""
#     else:
#         checkin_date_str = f"""checkin_date = Date({checkin_date})
# API.set_checkin_date(checkin_date)"""
#
#     if checkout_date == "None":
#         checkout_date_str = """API.set_checkout_date("None")"""
#     else:
#         checkout_date_str = f"""checkout_date = Date({checkout_date})
# API.set_checkout_date(checkout_date)"""
#
#     t = f"""API.select_booking_type({booking_type})
# API.select_transportation({means_of_transportation})
# location_from = Loc({location_from})
# API.set_origin(location_from)
# location_to = Loc({location_to})
# API.set_destination(location_to)
# API.set_min_ticket_price({min_price_ticket})
# API.set_max_ticket_price({max_price_ticket})
# API.set_num_adults({num_adults})
# API.set_num_children({num_children})
# {departure_date_str}
# {return_date_str}
# hotel_location = Loc({location})
# API.set_hotel_location(hotel_location)
# {checkin_date_str}
# {checkout_date_str}
# API.set_num_rooms({num_rooms})
# API.select_room_type({room_type})
# API.set_min_room_price({min_price_room})
# API.set_max_room_price({max_price_room})
# API.search()"""
#     print("API:", t)
#     print("###")
#     return "Booking done"

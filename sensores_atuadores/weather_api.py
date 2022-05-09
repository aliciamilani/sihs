import requests, json 

api_key = "8f07ff954fb086ad185e46b3104fbaaa"
base_url = "https://api.openweathermap.org/data/2.5/weather?"
city_name = "Manaus"
complete_url = base_url + "appid=" + api_key + "&q=" + city_name


def get_weather():

    response = requests.get(complete_url) 
    resp = response.json() 

    if resp["cod"] != "404": 
        current_weather = resp["weather"][0]["main"]

        return current_weather    
    else: 
        return 0
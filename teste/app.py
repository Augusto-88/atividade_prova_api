import requests
import json
def chuchubeleza():
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": -26.4851,
        "longitude": -49.0713,
        "current":[
            "temperature_2m",
            "relative_humidity_2m",
            "apparent_temperature",
            "precipitation",
            "wind_speed_10m"
        ]
    }

    resposta = requests.get(url, params=params)

    if resposta.status_code == 200:
        dados = resposta.json()
    else:
        print("Erro")

    return dados
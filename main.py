import requests
from twilio.rest import Client

endpoint = "https://api.openweathermap.org/data/2.5/onecall"

account_sid = "AC4c6e2c531157a7e579ee5915c372818a"
auth_token = "e51fb3180f0caa014631b0338307a635"
twilio_number = "+12056276309"

weather_params = {
    "lat": 23.800146,
    "lon": 91.280508,
    "appid": "62df2ca21ab91bcb77e26401d7e950b8",
    "exclude": "minutely,daily,current"
}

response = requests.get(endpoint, params=weather_params)

response_data = response.json()["hourly"][:12]

need_umbrella = False

for hour in response_data:
    weather_id = hour["weather"][0]["id"]
    print(weather_id)
    if weather_id < 700:
        need_umbrella = True
        break

if need_umbrella:
    client = Client(account_sid, auth_token)

    client.messages.create(
                                body="Chati loiya zaa bal",
                                from_=twilio_number,
                                to='+918415957390'
                            )


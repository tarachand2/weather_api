import requests
from twilio.rest import Client
api_key = "2b5a3beb6375e2c418cd04366c68cdb6"
api_endpoint = "https://api.openweathermap.org/data/2.5/weather"
account_sid = "ACb9b7260a5997fb2ba26b23c7691bf20d"
auth_token = "24067599415074994f6ecef18f054546"
params = {
    "lat": 54.76694444,
    "lon": 74.00027778,
    "appid": api_key
}
will_rain = False
response = requests.get(url=api_endpoint, params=params)
weather_data = response.json()
weather_code = weather_data["weather"][0]["id"]
print(weather_code)
if int(weather_code) < 700:
    will_rain = True
else:
    print("No need to bring umbrella.")

will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                         body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                         from_="+15737992721",
                         to="+919136248458"
                     )

    print(message.status)


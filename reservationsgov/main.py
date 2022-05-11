import requests as re
from twilio.rest import Client
import time
from flask import Flask
from datetime import datetime



def send_message(campsite):
    account_sid = 'ACd82c4ef1671f09f062624c17760fcd27'
    auth_token = '82ad47472ca8ec2849135880c40f44ea'
    client = Client(account_sid, auth_token)

    message = client.messages.create(body="https://www.recreation.gov/camping/campgrounds/232498/availability | " + campsite, from_="+14243724240", to='+16504555344')

app = Flask(__name__)

@app.route('/check')
def check_campsites():
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    r = re.get("https://www.recreation.gov/api/camps/availability/campground/232498/month?start_date=2021-07-01T00%3A00%3A00.000Z", headers=headers)
    print("Checking campsite")

    try:
        data = r.json()["campsites"]
        
        for campsite in data.keys():
            if data[campsite]["availabilities"]["2021-07-17T00:00:00Z"] != "Reserved":
                send_message(campsite)
                return "Success!!!!"
    except:
        return "Rate limited :("

    return "Nothing found :("
    

@app.route('/health-check')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Healthy'

@app.route('/')
def test():
    return "Test success"

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    print("Starting up")
    send_message("Hi")
    app.run(host='127.0.0.1', port=8080, debug=True)

# [END gae_python3_app]
# [END gae_python38_app]

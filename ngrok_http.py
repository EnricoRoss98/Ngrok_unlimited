from datetime import datetime
import json
import os
import requests
import threading
import time

url = 'CLOUD_FUNCTION_URL_FOR_UPDATE_DATA'


def temp():
    os.system("ngrok http https://localhost:9090")


time.sleep(20)
while True:
    try:
        x = threading.Thread(target=temp)
        x.start()

        time.sleep(5)

        # s = requests.Session()
        a = requests.get("http://127.0.0.1:4040/api/tunnels").text
        b = json.loads(a)
        c = str(b['tunnels'][0]['public_url'])

        r = requests.post(url, data={'data': json.dumps({'value': c, 'time': str(datetime.now())})})

        full_time = 3600 * 5
        # full_time = 10

        time.sleep(full_time)
        os.system("pkill ngrok")
        time.sleep(10)

    except:
        print("Error: unable to start thread")
        os.system("pkill ngrok")
        time.sleep(5)

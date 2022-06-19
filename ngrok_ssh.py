from datetime import datetime
import json
import os
import requests
import threading
import time

url = 'CLOUD_FUNCTION_URL_FOR_UPDATE_DATA'

def temp():
    os.system("ngrok tcp 22")

while True:
    try:
        x = threading.Thread(target = temp)
        x.start()

        time.sleep(5)

        # s = requests.Session()
        a = requests.get("http://127.0.0.1:4040/api/tunnels").text
        b = json.loads(a)
        c = str(b['tunnels'][0]['public_url'])

        c = c[6:]
        url_save = c.split(":")[0]
        port = c.split(":")[1]
        to_save = "ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@"+url_save+" -p "+port

        r = requests.post(url, data={'data': json.dumps({'value': to_save, 'time': str(datetime.now())})})

        full_time = 3600 * 7
        # full_time = 10

        time.sleep(full_time)
        os.system("pkill ngrok")
        time.sleep(10)

    except:
        print("Error: unable to start thread")
        os.system("pkill ngrok")
        time.sleep(5)

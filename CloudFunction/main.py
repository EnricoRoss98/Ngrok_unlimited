def read_data_ssh(request):
    from google.cloud import firestore

    try:
        value = ""
        time = ""
        db = firestore.Client()
        for doc in db.collection('ngrok').stream():
            values = doc.to_dict()
            if int(doc.id) == 0:
                time = str(values['time']).split(".")[0]
                value = str(values['value'])
                out = '<html><body>'+value+'<br><br>'+time+'</body></html>'
                return out
    except:
        pass


def read_data_https(request):
    from google.cloud import firestore

    try:
        value = ""
        db = firestore.Client()
        for doc in db.collection('ngrok').stream():
            values = doc.to_dict()
            if int(doc.id) == 1:
                value = str(values['value'])
                out = '<html><body onload=\'location.href="'+value+'"\'></body></html>'
                return out
    except:
        pass


def update_data(request):
    from google.cloud import firestore
    import json
    if request.method == 'OPTIONS':
        print('------ options')
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET,POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'Access-Control-Allow-Credentials': 'true'
        }
        return ('', 204, headers)

    request_json = json.loads(request.values['data'])
    # request_json = request.data.decode('utf-8')
    print('>>>>>>>>>>>>>>>>>>>>>>>')
    print(request_json)
    # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    if request_json['value'].startswith('ssh'):
        db = firestore.Client()
        to_save = {'value': request_json['value'], 'time': request_json['time']}
        db.collection('ngrok').document("0").set(to_save)
        return ('ok', 200, headers)
    elif request_json['value'].startswith('http'):
        db = firestore.Client()
        to_save = {'value': request_json['value'], 'time': request_json['time']}
        db.collection('ngrok').document("1").set(to_save)
        return ('ok', 200, headers)
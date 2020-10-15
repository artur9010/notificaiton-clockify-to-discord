import requests, json, os
from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/webhook", methods=['POST'])
def respond():
    if not request.is_json:
        print("Not json.")
        return Response(status=500)

    cj = request.json
    print(cj)
    
    pname = "-"
    if cj['project'] is not None:
        pname = cj['project']['name']

    cdesc = "-"
    if cj['description'] != "":
        cdesc = cj['description']

    cstart = cj['timeInterval']['start']

    cend = "Currently working"
    if cj['timeInterval']['end'] is not None:
        cend = cj['timeInterval']['end']
    
    dj = {
        "username": "Clockify",
        "embeds": [
            {
                "title": "Clockify - " + cj['user']['name'],
                "fields": [
                    {
                        "name": "Project name",
                        "value": pname,
                        "short": True
                    },
                    {
                        "name": "Description",
                        "value": cdesc,
                        "short": True
                    },
                    {
                        "name": "Start date",
                        "value": cstart,
                        "short": True
                    },
                    {
                        "name": "End date",
                        "value": cend,
                        "short": True
                    },
                ]
            },
        ]
    }

    r = requests.post(
        os.environ['WEBHOOK'],
        headers = {"Content-Type": "application/json"},
        data = json.dumps(dj)
    )
    print(r.status_code)
    print(r.text)
    return Response(status=200)
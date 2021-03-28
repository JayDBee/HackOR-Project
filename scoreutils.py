import requests
import json



def addscore (u, s):
    userid = str(u)
    score = str(s)

        

    url = "https://us-central1-aiot-fit-xlab.cloudfunctions.net/hackception"

    pl = {}
    pl['score'] = score
    pl['userid'] = userid
    pl['action'] = "addscore"

    payload = json.dumps(pl)

    # payload = "{\"score\" : \"22\",\r\n\"userid\" : \"1\",\r\n\"action\" : \"addscore\"}"
    
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)


def getallscores ():

    url = "https://us-central1-aiot-fit-xlab.cloudfunctions.net/hackception"

    pl = {}
    pl['action'] = "getallscores"

    payload = json.dumps(pl)

    # payload = "{\"score\" : \"22\",\r\n\"userid\" : \"1\",\r\n\"action\" : \"addscore\"}"
    
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

    res = json.loads(response.text)

    print (res)

    return res['scores']








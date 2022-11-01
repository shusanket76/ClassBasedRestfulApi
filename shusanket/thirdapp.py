import requests
import json
url = "http://127.0.0.1:8000/api"
daa = {
    "name":"RAM",
    "address":"THOKARPA"
}

jso = json.dumps(daa)
header={"content-Type":"application/json"}
r = requests.post(url=url, data=jso, headers=header)
print(r)
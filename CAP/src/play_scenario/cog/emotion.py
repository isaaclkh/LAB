#!/usr/bin/env python3
#-*- codig: utf-8 -*-
import sys
import requests
import json
client_id = "zq90hxu84o"
client_secret = "B6jHEYSIrkCK4kTVbK8l1NXclQAUcnBu7bRXcEoo"
url = "https://naveropenapi.apigw.ntruss.com/sentiment-analysis/v1/analyze"

headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret,
    "Content-Type": "application/json"
}

content = "친구랑 싸웠어 짜증나"

data = {
    "content": content
}

print(json.dumps(data, indent=4, sort_keys=True))
response = requests.post(url, data=json.dumps(data), headers=headers)
rescode = response.status_code

if (rescode == 200):
    print(response.json().get('document').get('sentiment'))

else:
    print("Error : " + response.text)

import json
import requests

client_id = "zq90hxu84o" # naver cloud platform - clova sentiment client id
client_secret = "B6jHEYSIrkCK4kTVbK8l1NXclQAUcnBu7bRXcEoo" # clova sentiment client password
url = "https://naveropenapi.apigw.ntruss.com/sentiment-analysis/v1/analyze" # naver sentiment url

# naver clova sentiment header
headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret,
    "Content-Type": "application/json" # jason 형식
}


data = {
    "content": "친구랑 싸웠는데 맛있는 밥을 먹어서 다시 잘 지내게 되었어. 근데 과제가 너무 많아서 밤을 새야할 것 같아. 그래서 너무 걱정이야. 그래도 친구랑 잘 해결되서 다행인 것 같아."
}

response = requests.post(url, data=json.dumps(data), headers=headers)
rescode = response.status_code
parse = response.json().get('document').get('sentiment')

if (rescode == 200):
    print(parse)

else:
    print("Error : " + response.text)
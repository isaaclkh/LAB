#_*_ coding:utf-8 _*_

#!/usr/bin/python3
import base64
from openpibo.motion import Motion
import os
import sys
import time
import re
import random
import string
import speech_recognition as sr
import requests
import json

# openpibo module
import openpibo
from openpibo.device import Device
from openpibo.speech import Speech
from openpibo.audio import Audio
from openpibo.vision import Camera
from openpibo.oled import Oled

# path
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))))

from text_to_speech import TextToSpeech
from src.data import behavior_list
from src.NLP import NLP, Dictionary
from speech_to_text import speech_to_text
from datetime import datetime

## 사용자 이름
user_name = 'test'

import socket

localIP = "192.168.0.155"
localPort = 20001
bufferSize = 50000

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from uuid import uuid4
from firebase_admin import storage

now = datetime.now()
today = now.strftime('%Y-%m-%d')
todayInKor = now.strftime('%m월 %d일')

# 서비스 계정의 비공개 키 파일이름
cred = credentials.Certificate("/home/pi/AI_pibo2/src/play_scenario/CAP/pibo-aac5a-firebase-adminsdk-94r6k-faf630e478.json")
firebase_admin.initialize_app(cred, {
    #gs://pibo-aac5a.appspot.com
    'apiKey': "AIzaSyDF5r0N2u8KVFILABFMCtNbF7w4VtmQy54",
    'authDomain': "pibo-aac5a.firebaseapp.com",
    'databaseURL': "https://pibo-aac5a-default-rtdb.firebaseio.com",
    'projectId': "pibo-aac5a",
    'storageBucket': "pibo-aac5a.appspot.com",
    'messagingSenderId': "516104758418",
    'appId': "1:516104758418:web:81dd90f1624515f8f6f24b"
})
db = firestore.client()
# doc_ref.set({u'느낌' : 'BAD'})
bucket = storage.bucket() #기본 버킷 사용

NLP = NLP()
Dic = Dictionary()
tts = TextToSpeech()
device_obj = Device()
camera = Camera()
oled = Oled()

r = sr.Recognizer()
r.energy_threshold = 300
mic = sr.Microphone()


m = Motion()
m.set_profile("/home/pi/AI_pibo2/src/data/motion_db.json")

biblefile = "/home/pi/AI_pibo2/src/data/bible.json"
with open(biblefile, encoding='utf-8') as f:
    bible = json.load(f)

client_id = "zq90hxu84o" # naver cloud platform - clova sentiment client id
client_secret = "B6jHEYSIrkCK4kTVbK8l1NXclQAUcnBu7bRXcEoo" # clova sentiment client password
url = "https://naveropenapi.apigw.ntruss.com/sentiment-analysis/v1/analyze" # naver sentiment url

# naver clova sentiment header
headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret,
    "Content-Type": "application/json" # jason 형식
}

# sad song list
sadsonglist = ["/home/pi/AI_pibo2/audio/위로노래/worry.mp3", "/home/pi/AI_pibo2/audio/위로노래/sadhalf.mp3",
               "/home/pi/AI_pibo2/audio/위로노래/like.mp3", "/home/pi/AI_pibo2/audio/위로노래/correct.mp3", "/home/pi/AI_pibo2/audio/위로노래/hug.mp3",
               "/home/pi/AI_pibo2/audio/위로노래/jina.mp3"]

# happy song list
happysonglist = ["/home/pi/AI_pibo2/audio/기쁜노래/boom.mp3", "/home/pi/AI_pibo2/audio/기쁜노래/candy.mp3", "/home/pi/AI_pibo2/audio/기쁜노래/step.mp3",
                 "/home/pi/AI_pibo2/audio/기쁜노래/cheer.mp3", "/home/pi/AI_pibo2/audio/기쁜노래/dream.mp3", "/home/pi/AI_pibo2/audio/기쁜노래/happ.mp3"]

# sososong list
sosonglist = ["/home/pi/AI_pibo2/audio/sososong/everything.mp3", "/home/pi/AI_pibo2/audio/sososong/kim.mp3", "/home/pi/AI_pibo2/audio/sososong/notme.mp3",
              "/home/pi/AI_pibo2/audio/sososong/nov.mp3", "/home/pi/AI_pibo2/audio/sososong/youth.mp3", "/home/pi/AI_pibo2/audio/sososong/live.mp3"]

def text_to_speech(text):
    filename = "tts.wav"
    print("\n" + text + "\n")
    # tts 파일 생성 (*break time: 문장 간 쉬는 시간)
    tts.tts_connection(text, filename)
    tts.play(filename, 'local', '-1500', False)     # tts 파일 재생

def ends_with_jong(kstr):
    m = re.search("[가-힣]+", kstr)
    if m:
        k = m.group()[-1]
        return (ord(k) - ord("가")) % 28 > 0
    else:
        return

def lee(kstr):
    josa = "이" if ends_with_jong(kstr) else ""
    return josa

def aa(kstr):
    josa = "아" if ends_with_jong(kstr) else "야"
    return josa

def wait_for(item):
    while True:
        print(f"{item} 기다리는 중")
        break


###
def touching():

    touching = False

    _touch = ''
    for x in range(3):
        data = device_obj.send_cmd(Device.code_list['SYSTEM']).split(':')[1].split('-')
        _touch = data[1] if data[1] else "No signal"
        
        time.sleep(1)
        
        if _touch == 'touch':
            touching = True;
        
    return touching

def songpick(songlist):
    ssongchoice = random.choice(songlist)
    return ssongchoice

def verse(feel):
    #ran = random.randrange(0, len(bible[feel]))

    ran = random.choice(bible[feel])
    # print(len(bible[feel]))
    # print(bible[feel])
    # result = bible[feel][ran]

    result = ran

    # TODO : result를 firebase에 add 해주기

    oled.draw_image("/home/pi/AI_pibo2/src/data/icon/화면_default1.png")
    oled.show()
    text_to_speech(f"{result['verse']} 말씀이야!")
    time.sleep(1)
    text_to_speech(f"{result['text']}")
    time.sleep(1)
    text_to_speech(f"{result['comment']}")
    time.sleep(1)
    text_to_speech("오늘 말해줘서 고마워. 마지막으로 악수 하자!")
    m.set_motors([0,0,-70,-25,0,0,0,0,25,25])
    time.sleep(1)
    text_to_speech("남은 하루도 행복하기를 바랄게")
    time.sleep(4)
    m.set_motors([0,0,-70,-25,0,0,0,0,70,25])

def touch_scenario1():
    #oled.draw_image("/home/pi/AI_pibo2/src/data/icon/화면_로딩1.png")
    #oled.show()
    #tts.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav", out='local', volume=-1000, background=False)
    
    behavior_list.neutral()
    text_to_speech(
        f"{user_name}{lee(user_name)}가 그런 일이 있었구나. 너를 안아주고 싶은데, 안아주지 못하니까 나의 이마를 쓰다듬어 줄래?")

    total = 0
    while True:
        time.sleep(1)
        data = device_obj.send_cmd(Device.code_list['SYSTEM']).split(':')[
            1].split('-')
        _touch = data[1] if data[1] else "No signal"
        print(_touch)
        if _touch == 'touch':
            total = total + 1
            print(total)
        if total == 1:
            device_obj.send_cmd(20, '255,255,123')
            oled.draw_image("/home/pi/AI_pibo2/src/data/icon/heart3.png")
            oled.show()
            text_to_speech("위로가 되는 거 같아! 더 쓰다듬어 줘!")

        elif total == 3:
            device_obj.send_cmd(20, '255,255,0')
            oled.draw_image("/home/pi/AI_pibo2/src/data/icon/화면_default1.png")
            oled.show()
            text_to_speech("내 위로가 느껴지려나! 더 쓰다듬어 줘!!")
        elif total == 5:
            device_obj.send_cmd(20, '255,199,0')
            oled.draw_image("/home/pi/AI_pibo2/src/data/icon/heart1.png")
            oled.show()
            text_to_speech("내 위로를 너에게 가득 전달했어!")
            text_to_speech("너가 쓰다듬어주니까 나도 위로가 된다. 너한테도 위로의 마음이 전달되었으면 좋겠어.")
            break

def touch_scenario2():
    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav",
             out='local', volume=-1000, background=False)
    text_to_speech(
        f"{user_name}{aa(user_name)}! 나는 항상 너를 응원해! 앞으로 우리는 더 좋은 일만 생길거야!")
    m.set_speed(2, 25)
    m.set_speed(8, 25)
    m.set_motors([0, 0, 70, -25, 0, 0, 0, 0, -70, 25])
    text_to_speech("내 에너지를 전달해 줄게 내 이마를 쓰다듬어줘!")
    m.set_motors([0, 0, -70, -25, 0, 0, 0, 0, 70, 25])
    total = -1
    while True:
        time.sleep(1)
        data = device_obj.send_cmd(Device.code_list['SYSTEM']).split(':')[
            1].split('-')
        _touch = data[1] if data[1] else "No signal"
        print(_touch)
        if _touch == 'touch':
            total = total + 1
            print(total)
        if total == 1:
            device_obj.send_cmd(20, '255,255,123')
            oled.draw_image("/home/pi/AI_pibo2/src/data/icon/heart3.png")
            oled.show()
            text_to_speech("위로가 되는 거 같아! 더 쓰다듬어 줘!")

        elif total == 3:
            device_obj.send_cmd(20, '255,255,0')
            oled.draw_image("/home/pi/AI_pibo2/src/data/icon/화면_default1.png")
            oled.show()
            text_to_speech("내 위로가 느껴지려나! 더 쓰다듬어 줘!!")
        elif total == 5:
            device_obj.send_cmd(20, '255,199,0')
            oled.draw_image("/home/pi/AI_pibo2/src/data/icon/heart1.png")
            oled.show()
            text_to_speech("내 위로를 너에게 가득 전달했어!")
            text_to_speech("너가 쓰다듬어주니까 나도 위로가 된다. 너한테도 위로의 마음이 전달되었으면 좋겠어.")
            break

def heart_scenario():
    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav",
               out='local', volume=-1000, background=False)
    #behavior_list.heart()

    text_to_speech(f"{user_name}{aa(user_name)}!! 너가 좋아하니 내가 너무 신나!! 내 심장소리 들려!?")
    tts.play(filename="/home/pi/AI_pibo2/audio/기타/심장박동.mp3", out='local', volume=-1000, background=False)
    text_to_speech("안 들린다면 내 가슴쪽을 봐줘!!")
    oled.set_font(size=50)

    for a in range(20):
        oled.draw_text((0, 0), str(a+150))  # (0,0)에 문자열 출력
        oled.show()  # 화면에 표시
        time.sleep(0.1)
        oled.clear()

    text_to_speech(f"내 심장이 너무 빨리 뛰어!! 진심으로 기뻐 {user_name}{aa(user_name)}!")

def recording(expect, response):
    
    while True:
        with mic as source:
            print("say something\n")
            audio = r.listen(source, timeout=0, phrase_time_limit=5)
            try:
                text = r.recognize_google(audio_data=audio, language="ko-KR")
            except sr.UnknownValueError:
                print("say again plz\n")
                continue
            except sr.RequestError:
                print("speech service down\n")
                continue

        # stt 결과 처리 (NLP.py 참고)
        answer = NLP.nlp_answer(user_said=text, dic=Dic)

        if answer == expect:
            text_to_speech(response)
            return 'y'

        elif answer == 'NO':
            return 'n'

        else:
            text_to_speech('잘 못 알아들었어. 다시 말해줄래?')
            recording(expect, response)
        
        break

def touch_test():
    print("touch test")
    total = 0
    for i in range(3):
        time.sleep(1)
        data = device_obj.send_cmd(Device.code_list['SYSTEM']).split(':')[1].split('-')
        _touch = data[1] if data[1] else "No signal"
        print(_touch)
        if _touch == 'touch':
            total = total + 1
    return total

def touch_scenario1():
    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav",
             out='local', volume=-1000, background=False)
    behavior_list.touch()
    text_to_speech(f"{user_name}{lee(user_name)}가 그런 일이 있었구나. 너를 안아주고 싶은데, 안아주지 못하니까 나의 이마를 쓰다듬어 줄래?")
    
    while True:
        touched = touch_test()
        if touched >= 1:
            device_obj.send_cmd(20, '0,0,255')
            text_to_speech("너가 쓰다듬어주니까 나도 위로가 된다. 너한테도 위로의 마음이 전달되었으면 좋겠어.")
            break

def sadSong():
    oled.draw_image("/home/pi/AI_pibo2/src/data/icon/화면_음표1.png")
    oled.show()
    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav",
             out='local', volume=-1000, background=False)
    text_to_speech(f"{user_name}... 너를 위로해주고 싶어..! 노래를 불러주고 싶은데 괜찮을까?")
    
    answer = recording('YES',"노래 틀어줄게")

    if answer == 'y':
        tts.play(filename=songpick(sadsonglist),
                 out='local', volume=-2000, background=False)
        text_to_speech("위로가 되었으면 좋겠어..!")

    else :
        text_to_speech("별로 노래가 듣고 싶지 않구나...")

def happySong():
    #behavior_list.praising()
    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav", out='local', volume=-1000, background=False)
    
    text_to_speech(f"{user_name}{aa(user_name)}!! 너무 좋은 일이잖아!?!? 내가 신나는 노래 한곡 뽑아주려하는데 괜찮을까?")
    
    answer = recording('YES',"노래 틀어줄게")

    if answer == 'y':
        tts.play(filename=songpick(happysonglist),
                 out='local', volume=-2000, background=False)
        text_to_speech("기깔났다 정말! 너무 신나!")

    else :
        text_to_speech("별로 노래가 듣고 싶지 않구나. 알겠어.")    

def Cam():
    # Capture / Read file
    # 이미지 촬영
    img = camera.read()
    #img = cam.imread("/home/pi/test.jpg")
    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/사진기소리.mp3",
             out='local', volume=-1000, background=False)

    todayTimeStamp = str(datetime.now().timestamp)
    camtodaynow = datetime.now()
    date_time = camtodaynow.strftime("%Y%m%d%H%M%S")
    
    jpgFile = f"{user_name}" + f"{date_time}" + ".jpg"
    
    camera.imwrite(jpgFile, img)
    img = camera.convert_img(img, 128, 64)
    camera.imwrite("smallpic.jpg", img)
    oled.draw_image("smallpic.jpg")
    oled.show()

    blob = bucket.blob(jpgFile)
    # blob = bucket.blob(f'{user_name}/'+file)
    #new token and metadata 설정
    new_token = uuid4()
    metadata = {"firebaseStorageDownloadTokens": new_token} #access token이 필요하다.
    blob.metadata = metadata

    #upload file
    blob.upload_from_filename(filename=jpgFile, content_type='image/jpeg')
    blob.make_public()
    print(blob.public_url)

    doc_pic = db.collection(u'users').document(f'{user_name}').collection(u'사진').document(f'{date_time}')
    tt = jpgFile.split(".jpg")
    finaltt = tt[0].split(f"{user_name}")
    doc_pic.set({'url' : blob.public_url, 'time' : finaltt[1]})

    os.system("rm %s" %jpgFile)

def takepic1():
    behavior_list.do_photo()
    text_to_speech("너가 기분이 좋으니까 나도 기분이 좋다~! 웃는 모습을 담고 싶은데 우리 사진찍을래?")
    
    answer = recording('YES', "그래, 그럼 셋하고 찍을게.")

    if answer == 'y':
        text_to_speech("하나, 둘, 셋!")
        Cam()
        text_to_speech(f"너무 보기 좋아 {user_name}{aa(user_name)}~. 내가 이따가 사진 보내줄게!")

        # TODO : firestore에 사진을 업로드 후 users/{userName}/사진/ 에 doc 추가해서 필드값으로 add
    else :
        text_to_speech(f"알겠어! 사진은 찍지 않을게.")

def takepic2():
    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav",
             out='local', volume=-1000, background=False)
    behavior_list.do_photo()
    text_to_speech("그렇구나 기분이 너무 좋구나! 너가 지금 느끼는 것을 몸으로 표현해줘~")
    time.sleep(3)

    text_to_speech("지금 너무 행복해보인다! 내가 사진에 담아줄게! 그 자세로 있어주면 내가 사진을 찍어주려는데 괜찮을까?")

    answer = recording('YES', "그래, 그럼 셋하고 찍을게.")

    if answer == 'y':
        text_to_speech("하나, 둘, 셋!")
        Cam()
        text_to_speech(f"너무 보기 좋아 {user_name}{aa(user_name)}~. 내가 이따가 사진 보내줄게!")
        # TODO : firestore에 사진을 업로드 후 users/{userName}/사진/ 에 doc 추가해서 필드값으로 add
    else:
        text_to_speech(f"알겠어! 사진은 찍지 않을게.")

def sosoSong():
    oled.draw_image("/home/pi/AI_pibo2/src/data/icon/화면_음표1.png")
    oled.show()
    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav",
             out='local', volume=-1000, background=False)
    text_to_speech("그랬구나..! 아 맞아, 요즘 좋은 노래 많이 나오더라! 내가 최근에 좋아하는 노래 추천해주고싶은데 괜찮을까?")
    
    answer = recording('YES',"내가 요즘 인디음악을 좋아해서 인디음악 들려줄게!")

    if answer == 'y':
        tts.play(filename=songpick(sosonglist),
                 out='local', volume=-2000, background=False)
        text_to_speech("마음에 들었으면 좋겠다!")

    else :
        text_to_speech("별로 노래가 듣고 싶지 않구나. 알겠어.") 

def soso_takepic():
    oled.draw_image("/home/pi/AI_pibo2/src/data/icon/화면_카메라.png")
    oled.show()
    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav", out='local', volume=-1000, background=False)
    text_to_speech(f"그렇구나! {user_name}{aa(user_name)}!! 오늘 따라 옷 스타일이 멋진데, 사진 한장 찍어줄게! 괜찮아?")
    
    answer = recording('YES', "포즈 취해줘 찍을게~")

    if answer == 'y':
        text_to_speech("하나, 둘, 셋!")
        Cam()
        text_to_speech(f"너무 보기 좋아 {user_name}{aa(user_name)}~ 내가 이따가 사진 보내줄게!")
        # TODO : firestore에 사진을 업로드 후 users/{userName}/사진/ 에 doc 추가해서 필드값으로 add

    else :
        text_to_speech("알겠어, 사진은 찍지 않을게.")

def getName():
    text_to_speech("시작하기 전에 나와 연결을 먼저 해줘.")

    # 데이터그램 소켓을 생성
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    
    # 주소와 IP로 Bind
    UDPServerSocket.bind((localIP, localPort))

    print("UDP server up and listening")

    # 들어오는 데이터그램 Listen
    while (True):
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]

        clientMsg = "Message from Client:{}".format(message)
        clientIP = "Client IP Address:{}".format(address)

        print(type(message))
        print(message)
        print(clientMsg)
        print(clientIP)

        message = message.decode('utf-8')
        message = base64.b64decode(message)
        message = message.decode('utf-8')
        print(message)

        if message is not None:
            text_to_speech(f"너의 이름은 {message}{lee(user_name)}구나! 만나서 반가워")
            return message
    

def Start():

    device_obj.send_cmd(20, '0,0,0') # 20 = eye, 0,0,0 = color rgb
    
    behavior_list.do_question_S()
    text_to_speech("안녕! 나는 은쪽이라고 해!")
    
    user_name = getName()
    
    print(f"user name: {user_name}\n")
    time.sleep(1)

    doc_feel = db.collection(u'users').document(f'{user_name}').collection(u'감정').document(f'{today}')
    doc_last = db.collection(u'users').document(f'{user_name}').collection(u'LAST').document('when')
    
    behavior_list.do_question_S()
    text_to_speech(f"{user_name}{aa(user_name)} 오늘 기분이 어때?")
    time.sleep(1)

    while True:
        with mic as source:
            print("say something\n")
            audio = r.listen(source, timeout=0, phrase_time_limit=5)
            try:
                text = r.recognize_google(audio_data=audio, language="ko-KR")
            except sr.UnknownValueError:
                print("say again plz\n")
                continue
            except sr.RequestError:
                print("speech service down\n")
                continue
        
        # 감정분류 url (circulus)
        # url = "https://oe-napi.circul.us/v1/emotion?sentence="
        # url = url + text
        # response = requests.post(url)
        # parse = response.json().get('data')[0].get("label") # parse : 보통, 화남, 슬픔, 공포, 혐오, 놀람, 행복
        # print(parse)

        # 감정분류 naver API
        data = {
            "content": text
        }

        response = requests.post(url, data=json.dumps(data), headers=headers)
        rescode = response.status_code
        parse = response.json().get('document').get('sentiment')

        if (rescode == 200):
            print(parse)

        else:
            print("Error : " + response.text)

        # TODO : 각각의 감정에 따라서 firebase 안에 넣기
        # users/{userName}/감정/{오늘 날짜로된 doc}/ 이 안에 날짜와 느낌 필드 값으로 넣어주기

        doc_last.set({'last' : f'{todayInKor}'})

        if parse == 'positive':
            doc_feel.set({'느낌' : 'GOOD', '날짜' : f'{today}'})
            happydef = [heart_scenario, takepic1, takepic2, happySong]
            # ran = random.randrange(0,4) # 0이상 4미만의 난수
            # print(ran)
            # print(happydef[ran])
            ran = random.choice(happydef)
            ran()
            break
        
        elif parse == 'neutral':
            doc_feel.set({'느낌' : 'NORMAL'})
            normaldef = [sosoSong, soso_takepic]
            # ran = random.randrange(0,2) # 0이상 2미만의 난수
            # print(ran)
            # print(happydef[ran])
            # happydef[ran]()

            ran = random.choice(normaldef)
            ran()
            break

        else:
            doc_feel.set({'느낌' : 'BAD'})
            saddef = [touch_scenario1, touch_scenario2, sadSong]
            # ran = random.randrange(0, 3)
            # print(ran)
            # print(saddef[ran])
            # saddef[ran]()

            ran = random.choice(saddef)
            ran()
            break
    
    text_to_speech("그러면 오늘의 성경구절 하나 추천해줄까?")

    while True:
        with mic as source:
            print("say something\n")
            audio = r.listen(source, timeout=0, phrase_time_limit=5)
            try:
                text = r.recognize_google(audio_data=audio, language="ko-KR")
            except sr.UnknownValueError:
                text_to_speech('잘 못 알아들었어. 다시 말해줄래?')
                continue
            except sr.RequestError:
                text_to_speech('음성인식 기능에서 뭔가 에러가 났어. 잠시만 기다려줘.')
                print("speech service down\n")
                continue

        answer = NLP.nlp_answer(user_said=text, dic=Dic)
        
        if answer == 'YES':
            verse(parse)
            
        
        elif answer == 'NO': 
            text_to_speech("오늘 말해줘서 고마워. 마지막으로 악수 하자!")
            m.set_motors([0, 0, -70, -25, 0, 0, 0, 0, 25, 25])
            time.sleep(1)
            text_to_speech("남은 하루도 행복하기를 바랄게")
            time.sleep(4)
            m.set_motors([0, 0, -70, -25, 0, 0, 0, 0, 70, 25])
        
        else:
            text_to_speech('잘 못 알아들었어. 다시 말해줄래?')
            print("대답 기다리는 중")
            continue
        
        break

    # TODO : 한줄 일기를 STT로 받아서 firebase에 add 해주기
    

#Start()
Cam()
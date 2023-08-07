#!/usr/bin/python3
from anyio import sleep
from openpibo.motion import Motion
import os
import sys
import time
import random
import string
import requests
import json

from threading import Thread
from datetime import datetime

# openpibo module
import openpibo
from openpibo.device import Device
from openpibo.speech import Speech
from openpibo.audio import Audio
from openpibo.vision import Camera
from openpibo.oled import Oled

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from uuid import uuid4
from firebase_admin import storage

# path
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(
    os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))))

print(sys.path)
from src.text_to_speech import TextToSpeech
from src.NLP import NLP, Dictionary
from src.JongSung import ends_with_jong, lee, aa
from src.robotnetworking import clientToServer
from src.robotGPT import emotion, chatting
from src.textFinal import text_to_speech, stt
from src.data import behavior_list
import src.data.oled_list as oled

from src.activity.positive import happysong, happytalk, happydance
from src.activity.negative import sadsong, medy, drawing
from src.activity.neutral import midsong, midtalk

NLP = NLP()
Dic = Dictionary()
device_obj = Device()
camera = Camera()
tts = TextToSpeech()

m = Motion()
m.set_profile("/home/pi/PCAP/src/data/motion_db.json")

# 서비스 계정의 비공개 키 파일이름
cred = credentials.Certificate(
    "/home/pi/AI_pibo2/src/play_scenario/CAP/pibo-aac5a-firebase-adminsdk-94r6k-faf630e478.json")
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
bucket = storage.bucket()  # 기본 버킷 사용



global text

# def sendTo(message):
#     doc_topibo = db.collection(u'connectwithpibo').document('toPibo')
#     doc_frompibo = db.collection(u'connectwithpibo').document('fromPibo')

#     doc_frompibo.set({'msg': message})

def wait_for(item):
    while True:
        print(f"{item} 기다리는 중")
        break


localIP = "192.168.137.71"
localPort = 20001

user_name = '건호'

device_obj.send_cmd(20, '0,0,0')  # 20 = eye, 0,0,0 = color rgb
behavior_list.do_question_S("안녕! 나는 은쪽이라고 해, 만나서 반가워.")
# text_to_speech("시작하기 전에, 나와 연결을 먼저 해줘.")
# # user_name = clientToServer(localIP, localPort)
# text_to_speech(f"너의 이름은 {user_name}{lee(user_name)}구나! 만나서 반가워")
# text_to_speech("너를 더 알아가기 위해서 얘기를 하고 싶은데. 중간에 대화를 끊고 활동으로 넘어가고 싶으면 대화 종료 라고 말해줘.")
# print(user_name)
# text_to_speech(f"{user_name}{aa(user_name)} 오늘 뭐했어?")

# your_day = stt()
# em = emotion(your_day)
# text_to_speech(f"{em}")
# chatting(your_day)
# oled.o_heart()
midsong()

# if em == '긍정':
#     happydef =[happysong, happytalk, happypic, happydance]

#     ran = random.choice(happydef)
#     ran()

# elif em =='중립' :
#     neutraldef = [midtalk, midsong]

#     ran = random.choice(neutraldef)
#     ran()

# else em == '부정' :
#     saddef = [sadsong, medy, drawing]

#     ran = random.choice(saddef)
#     ran()
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

# path
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(
    os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))))

from src.text_to_speech import TextToSpeech
from src.NLP import NLP, Dictionary
from src.JongSung import ends_with_jong, lee, aa
from src.robotnetworking import clientToServer
from src.robotGPT import emotion, chatting
from src.textFinal import text_to_speech, stt
from src.data import behavior_list
import src.data.oled_list as oled

from src.activity.positive import happysong, happytalk, happydance, happypic
from src.activity.negative import sadsong, medi, drawing
from src.activity.neutral import midsong, midtalk

NLP = NLP()
Dic = Dictionary()
device_obj = Device()
camera = Camera()
tts = TextToSpeech()

m = Motion()
m.set_profile("/home/pi/PCAP/src/data/motion_db.json")

global text
global user_name

def wait_for(item):
    while True:
        print(f"{item} 기다리는 중")
        break


localIP = "192.168.0.155"
localPort = 20001

user_name = '건호'

def activities(emotion):
    global user_name

    # happydef =[happysong, happytalk, happypic, happydance]
    # neutraldef = [midtalk, midsong]
    # saddef = [sadsong, medy, drawing]

    activity = []
    
    if emotion == '긍정':
        activity = [happysong, happytalk, happypic, happydance]
    if emotion == '중립':
        activity = [midtalk, midsong]
    if emotion == '부정':
        activity = [sadsong, medi, drawing]
    
    ran = random.choice(activity)

    if ran == happypic :
        ran(user_name)
        activity.remove(ran)
    else :
        ran()
        activity.remove(ran)

    while len(activity) != 0 :
        text_to_speech("내가 다른 활동도 준비한 것이 있는데. 같이 해볼래?")
        ans = stt()

        if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES' :
            ran = random.choice(activity)

            if ran == happypic :
                happypic(user_name)
                activity.remove(ran)
                print("activity : ", activity)
            
            else :
                ran()
                activity.remove(ran)
                print("activity : ", activity)
        
        else :
            activity.clear()

def fin(emotion):
    
    if emotion == '긍정':
        text_to_speech("너랑 이야기 하니까 기분이 좋아졌어! 너는 어때?")
        ans = stt()

        if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES' :
            behavior_list.do_joy("너가 좋았다고하니 너무 기쁜걸!")

        else :
            behavior_list.do_sad("미안해, 앞으로 더 노력하는 내가 될게.")
        
        text_to_speech("너는 긍정적인 에너지가 넘치는 것 같아. 앞으로도 자주 이야기하자.")
        time.sleep(1)
        text_to_speech("오늘 너무 즐거웠어, 다음에 또 보자.")

        time.sleep(1)
        text_to_speech("마지막으로 악수 하자")
        behavior_list.do_shake_hands()
        text_to_speech("잘가")
    
    if emotion == '중립':
        text_to_speech("오늘 너랑 이야기할수 있어서 너무 좋았어. 너는 어땠어?")
        ans = stt()

        if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES' :
            behavior_list.do_joy("고마워, 나의 마음이 너에게 닿아서 다행이야!")

        else :
            behavior_list.do_sad("미안해, 앞으로 더 노력하는 내가 될게.")
        
        text_to_speech("언제든지 이야기 나누고 싶을 때 불러줘.")
        time.sleep(1)
        text_to_speech("마지막으로 악수 하자")
        behavior_list.do_shake_hands()
        text_to_speech("잘가")

    if emotion == '부정':
        text_to_speech("오늘은 조금 감정적으로 힘들었던 하루였네. 이런 시기도 지나가기 마련이야. 그래도 나랑 함께해서 조금 괜찮아지지 않았어?")
        ans = stt()

        if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES' :
            behavior_list.do_joy("고마워, 나의 마음이 너에게 닿아서 다행이야!")

        else :
            behavior_list.do_sad("미안해, 앞으로 더 노력하는 내가 될게.")
        
        text_to_speech("언제든지 내가 함께 할게, 다음에 힘들때도 나한테 와서 털어놔, 다음에 또 보자!")
        time.sleep(1)
        text_to_speech("마지막으로 포옹 하자")
        behavior_list.do_hug_me()
        text_to_speech("잘가")

device_obj.send_cmd(20, '0,0,0')  # 20 = eye, 0,0,0 = color rgb
behavior_list.do_question_S("안녕! 나는 은쪽이라고 해, 만나서 반가워.")
oled.o_heart()
text_to_speech("시작하기 전에, 나와 연결을 먼저 해줘.")
user_name = clientToServer(localIP, localPort)
text_to_speech(f"너의 이름은 {user_name}{lee(user_name)}구나! 만나서 반가워")
text_to_speech("너를 더 알아가기 위해서 얘기를 하고 싶은데. 중간에 대화를 끊고 활동으로 넘어가고 싶으면 대화 종료 라고 말해줘.")
print(user_name)
text_to_speech(f"{user_name}{aa(user_name)} 오늘 뭐했어?")

your_day = stt()

em = emotion(your_day)

print(f"감정 : {em}")

chatting(your_day)

oled.o_heart()
activities(em)
fin(em)


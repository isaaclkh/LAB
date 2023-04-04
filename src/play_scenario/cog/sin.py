#!/usr/bin/python3

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

NLP = NLP()
Dic = Dictionary()
tts = TextToSpeech()
device_obj = Device()
camera = Camera()
oled = Oled()

r = sr.Recognizer()
r.energy_threshold = 300
mic = sr.Microphone()
biblefile = "/home/pi/AI_pibo2/src/data/bible.json"
with open(biblefile, encoding='utf-8') as f:
    bible = json.load(f)
user_name = '진형'

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

def verse(feel):
    ran = random.randrange(0,len(bible[feel]))
    print(len(bible[feel]))
    print(bible[feel])
    result=bible[feel][ran]

    oled.draw_image("/home/pi/AI_pibo2/src/data/icon/화면_default1.png")
    oled.show()
    text_to_speech(f"{result['verse']} 말씀이야!")
    time.sleep(1)
    text_to_speech(f"{result['text']}")
    time.sleep(1)
    text_to_speech(f"{result['comment']}")
    time.sleep(1)
    text_to_speech(f"그래 오늘 수고 많았어. 나에게 말해줘서 고마워. 다음에도 너의 이야기를 들려줘!")


def heart_scenario():
    # behavior_list.heart()
    
    text_to_speech(
        f"{user_name}{aa(user_name)}!! 너가 좋아하니 내가 너무 신나!! 내 심장소리 들려!?")
    tts.play(filename="/home/pi/audio/기타/심장박동.mp3", out='local', volume=-100, background=False)
    text_to_speech(f"안 들린다면 내 가슴쪽을 봐줘!!")
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

            while True:
                text_to_speech(response)
                time.sleep(1)
                break
        else:

            wait_for(expect)    # DONE 답변 들어올 때까지 stt open 반복
            continue
        break


def touch_test():
    print(f"touch test")
    total = 0
    for i in range(3):
        time.sleep(1)
        data = device_obj.send_cmd(Device.code_list['SYSTEM']).split(':')[1].split('-')
        _touch = data[1] if data[1] else "No signal"
        if _touch == 'touch':
            total = total + 1
    return total


def touch_scenario1():
    # behavior_list.touch()
    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav",
             out='local', volume=-1000, background=False)
    text_to_speech(f"{user_name}{lee(user_name)}가 그런 일이 있었구나. 너를 안아주고 싶은데, 안아주지 못하니까 나의 이마를 쓰다듬어 줄래?")
    touched = touch_test()
    if touched > 1:
        device_obj.send_cmd(20, '0,0,255')
        text_to_speech(f"너가 쓰다듬어주니까 나도 위로가 된다. 너한테도 위로의 마음이 전달되었으면 좋겠어.")

def touch_scenario2():
    # behavior_list.touch()
    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav", out='local', volume=-1000, background=False)
    text_to_speech(f"{user_name}! 나는 항상 너를 응원해! 앞으로 우리는 더 좋은 일만 생길거야! 내 에너지를 전달해 줄게 내 이마를 쓰다듬어줘!")
    touched = touch_test()
    if touched > 1:
        device_obj.send_cmd(20,'0,0,255')
        text_to_speech(f"내 에너지를 방금 너에게 보냈어! 앞으로 좋은 일만 가득할거야! 아자아자!!")

def sadsong_scenario():
    oled.draw_image("/home/pi/AI_pibo2/src/data/icon/화면_음표1.png")
    oled.show()
    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav",
             out='local', volume=-1000, background=False)
    text_to_speech(f"{user_name}... 너를 위로해주고 싶어..! 노래를 불러주고 싶은데 괜찮을까?")
    recording('YES',"노래 틀어줄게")
    songlist = ["/home/pi/audio/위로노래/twice-cheer-up.mp3", "/home/pi/audio/위로노래/걱정말아요그대.mp3", "/home/pi/audio/위로노래/너의슬픔을오늘내가반을가져가줄게.mp3","/home/pi/audio/위로노래/말하는대로.mp3","/home/pi/audio/위로노래/우리가맞다는대답을할거예요.mp3","/home/pi/audio/위로노래/정준일-안아줘.mp3"]
    ran = random.randrange(0,6)
    tts.play(filename=songlist[ran], out='local', volume=-2000, background=False)
    text_to_speech(f"위로가 되었으면 좋겠어..!")
    

def Cam():
    # Capture / Read file
    # 이미지 촬영
    img = camera.read()
    #img = cam.imread("/home/pi/test.jpg")
    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/사진기소리.mp3",
             out='local', volume=-1000, background=False)
    # Write(test.jpg라는 이름을 촬영한 이미지 저장)
    camera.imwrite("pic.jpg", img)
    img = camera.convert_img(img, 128, 64)
    camera.imwrite("smallpic.jpg", img)
    oled.draw_image("smallpic.jpg")
    oled.show()

def happysong_scenario():
    # behavior_list.praising()
    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav", out='local', volume=-1000, background=False)
    text_to_speech(f"{user_name}{aa(user_name)}!! 너무 좋은 일이잖아!?!? 내가 신나는 노래 한곡 뽑아줄게! 괜찮을까!?")
    songlist = ["/home/pi/audio/신나는/blackpink-붐바야.mp3", "/home/pi/audio/신나는/hot-candy.mp3", "/home/pi/audio/신나는/kara-step.mp3"]
    ran = random.randrange(0,3)
    tts.play(filename=songlist[ran], out='local', volume=-2000, background=False)
    text_to_speech(f" 기깔났다 정말! 너무 신나! ")

def takepic1():
    # behavior_list.do_photo()
    text_to_speech(f"너가 기분이 좋으니까 나도 기분이 좋다~! 웃는 모습을 담고 싶은데 우리 사진찍을래?")
    recording('YES', "찍을게")
    Cam()
    text_to_speech(f"너무 보기 좋아 {user_name}~ 내가 이따가 사진 보내줄게!")


def takepic2():
    # behavior_list.do_photo()
    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav",
             out='local', volume=-1000, background=False)
    text_to_speech(f"그렇구나 기분 너무 좋겠다! 너가 지금 느끼는 것을 몸으로 표현해줘~")
    time.sleep(3)
    text_to_speech(f"지금 너무 행복해보인다! 내가 사진에 담아줄게! 그자세로 있어주면 내가 사진을 찍어줄게!")
    Cam()
    text_to_speech(f"너무 보기 좋아 {user_name}{aa(user_name)}~ 내가 이따가 사진 보내줄게!")

def emotion():
    print("emotion")


def Start():
    device_obj.send_cmd(20, '0,0,0') # 20 = eye, 0,0,0 = color rgb
    #device_obj.send_cmd(25, '2') 
    print(f"user name: {user_name} \n")
    time.sleep(1)
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

        # TODO : 현재 pibo 홈페이지 접속 불가로 감정 분류는 하지 못함 일단 사용자의 답변을 기다리는 것까지
        # 이것을 answer로 처리를 해서 if 어떠한 감정 => 그에 따른 분류
        
        # 감정분류 url
        url = "https://oe-napi.circul.us/v1/emotion?sentence="
        url = url + text
        response = requests.post(url)
        parse = response.json().get('data')[0].get("label") # parse : 보통, 화남, 슬픔, 공포, 혐오, 놀람, 행복
        print(parse)

        if parse == '행복':
            happydef = [heart_scenario, takepic1, takepic2,happysong_scenario]
            ran = random.randrange(0,4) # 0이상 3미만의 난수
            happydef[ran]()

        elif parse=='보통':
            # DONE 답변 들어올 때까지 stt open 반복
            text_to_speech("아! 그렇구나! 말해줘서 고마워")
            
        elif parse == '화남' or '슬픔' or '공포' or '혐오' or '놀람':
            ran = random.randrange(0,3)
            saddef = [touch_scenario1, touch_scenario2, sadsong_scenario]
            saddef[ran]()
            
        
            
        break

    text_to_speech(f"그러면 오늘의 성경구절 하나 추천해줄까?")
    while True:
        with mic as source:
            print("say something\n")
            audio = r.listen(source, timeout=0, phrase_time_limit=3)
            try:
                text = r.recognize_google(audio_data=audio, language="ko-KR")
            except sr.UnknownValueError:
                print("say again plz\n")
                continue
            except sr.RequestError:
                print("speech service down\n")
                continue

        
        answer = NLP.nlp_answer(user_said=text, dic=Dic)
        if answer == 'YES':
            if parse == '행복':
    
                verse('happiness')
            elif parse == '공포':
                verse('fear')
            elif parse == '놀람':
                verse('fear')
            elif parse == '화남':
                verse('angry')
            elif parse == '혐오':
                verse('angry')
        
            elif parse == '슬픔':
                verse('sadness')
            else:
                # DONE 답변 들어올 때까지 stt open 반복
                
                text_to_speech(f"그럼 오늘의 말씀 추천해 줄게")
                verse('neutral')
            break
        elif answer == 'NO':
            text_to_speech(f"그래 오늘 수고 많았어. 나에게 말해줘서 고마워. 다음에도 너의 이야기를 들려줘!")
        else:
            print("대답 기다리는 중")
            continue
        break

Start()



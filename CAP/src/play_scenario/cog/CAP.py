#!/usr/bin/python3
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

## 여기에 사용자 이름 넣기
user_name = '건호'

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
    #ran = random.randrange(0, len(bible[feel]))

    ran = random.choice(bible[feel])
    # print(len(bible[feel]))
    # print(bible[feel])
    # result = bible[feel][ran]

    result = ran

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

# def touch_scenario2():
#     tts.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav", out='local', volume=-1000, background=False)
#     behavior_list.touch()
#     text_to_speech(f"{user_name}! 나는 항상 너를 응원해! 앞으로 우리는 더 좋은 일만 생길거야! 내 에너지를 전달해 줄게, 내 이마를 쓰다듬어줘!")
    
#     while True:
#         touched = touch_test()
#         if touched >= 1:
#             device_obj.send_cmd(20, '0,0,255')
#             text_to_speech("내 에너지를 방금 너에게 보냈어! 앞으로 좋은 일만 가득할거야! 아자아자!!")
#             break

def sadSong():
    oled.draw_image("/home/pi/AI_pibo2/src/data/icon/화면_음표1.png")
    oled.show()
    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav",
             out='local', volume=-1000, background=False)
    text_to_speech(f"{user_name}... 너를 위로해주고 싶어..! 노래를 불러주고 싶은데 괜찮을까?")
    
    answer = recording('YES',"노래 틀어줄게")
    
    songlist = ["/home/pi/AI_pibo2/audio/위로노래/worry.mp3", "/home/pi/AI_pibo2/audio/위로노래/sadhalf.mp3",
                "/home/pi/AI_pibo2/audio/위로노래/like.mp3", "/home/pi/AI_pibo2/audio/위로노래/correct.mp3", "/home/pi/AI_pibo2/audio/위로노래/hug.mp3",
                "/home/pi/AI_pibo2/audio/위로노래/jina.mp3"]
    
    #ran = random.randrange(0,6) // 0-5

    ssongchoice = random.choice(songlist)
    
    if answer == 'y':
        tts.play(filename=ssongchoice, out='local', volume=-2000, background=False)
        text_to_speech("위로가 되었으면 좋겠어..!")

    else :
        text_to_speech("별로 노래가 듣고 싶지 않구나...")

def happySong():
    #behavior_list.praising()
    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav", out='local', volume=-1000, background=False)
    
    text_to_speech(f"{user_name}{aa(user_name)}!! 너무 좋은 일이잖아!?!? 내가 신나는 노래 한곡 뽑아줄게!")
    
    songlist = ["/home/pi/AI_pibo2/audio/기쁜노래/boom.mp3", "/home/pi/AI_pibo2/audio/기쁜노래/candy.mp3", "/home/pi/AI_pibo2/audio/기쁜노래/step.mp3",
                "/home/pi/AI_pibo2/audio/기쁜노래/cheer.mp3", "/home/pi/AI_pibo2/audio/기쁜노래/dream.mp3", "/home/pi/AI_pibo2/audio/기쁜노래/happ.mp3"]
    
    #ran = random.randrange(0,6) // 0-5
    #print(ran)

    #random.shuffle(songlist)
    hsongchoice = random.choice(songlist)
    
    tts.play(filename=hsongchoice, out='local', volume=-2000, background=False)
    
    text_to_speech("기깔났다 정말! 너무 신나!")

def Cam():
    # Capture / Read file
    # 이미지 촬영
    img = camera.read()
    #img = cam.imread("/home/pi/test.jpg")
    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/사진기소리.mp3",
             out='local', volume=-1000, background=False)
    
    camera.imwrite("/home/pi/pic.jpg", img)
    img = camera.convert_img(img, 128, 64)
    camera.imwrite("smallpic.jpg", img)
    oled.draw_image("smallpic.jpg")
    oled.show()


def takepic1():
    behavior_list.do_photo()
    text_to_speech("너가 기분이 좋으니까 나도 기분이 좋다~! 웃는 모습을 담고 싶은데 우리 사진찍을래?")
    
    answer = recording('YES', "찍을게")

    if answer == 'y':
        Cam()
        text_to_speech(f"너무 보기 좋아 {user_name}{aa(user_name)}~ 내가 이따가 사진 보내줄게!")
    else :
        text_to_speech(f"알겠어! 사진은 찍지 않을게, {user_name}{aa(user_name)}~")


def takepic2():
    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav",
             out='local', volume=-1000, background=False)
    behavior_list.do_photo()
    text_to_speech("그렇구나 기분이 너무 좋구나! 너가 지금 느끼는 것을 몸으로 표현해줘~")
    time.sleep(3)
    text_to_speech("지금 너무 행복해보인다! 내가 사진에 담아줄게! 그 자세로 있어주면 내가 사진을 찍어줄게!")
    Cam()
    text_to_speech(f"너무 보기 좋아 {user_name}{aa(user_name)}~ 내가 이따가 사진 보내줄게!")

def soso_scenario():
    oled.draw_image("/home/pi/AI_pibo2/src/data/icon/화면_음표1.png")
    oled.show()
    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav",
             out='local', volume=-1000, background=False)
    text_to_speech("그랬구나..! 아 맞아, 요즘 좋은 노래 많이 나오더라! 내가 최근에 좋아하는 노래 추천해주고싶은데 괜찮을까?")
    answer = recording('YES',"내가 요즘 인디음악을 좋아해서 인디음악 들려줄게!")
    
    songlist = ["/home/pi/AI_pibo2/audio/sososong/everything.mp3", "/home/pi/AI_pibo2/audio/sososong/kim.mp3", "/home/pi/AI_pibo2/audio/sososong/notme.mp3",
                "/home/pi/AI_pibo2/audio/sososong/nov.mp3", "/home/pi/AI_pibo2/audio/sososong/youth.mp3", "/home/pi/AI_pibo2/audio/sososong/live.mp3"]
    
    ran = random.randrange(0,6)

    if(answer=='y'):
        tts.play(filename=songlist[ran], out='local', volume=-2000, background=False)
        text_to_speech("마음에 들었으면 좋겠다!")
    else:
        text_to_speech("별로 음악이 듣고 싶지 않구나!")


def soso_takepic():
    oled.draw_image("/home/pi/AI_pibo2/src/data/icon/화면_카메라.png")
    oled.show()
    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav", out='local', volume=-1000, background=False)
    text_to_speech(f"그렇구나! {user_name}{aa(user_name)}!! 오늘 따라 옷 스타일이 멋진데, 사진 한장 찍어줄게! 괜찮아?")
    time.sleep(3)
    text_to_speech("포즈 취해줘 찍을게~")
    Cam()
    text_to_speech(f"너무 보기 좋아 {user_name}{aa(user_name)}~ 내가 이따가 사진 보내줄게!")

def Start():

    device_obj.send_cmd(20, '0,0,0') # 20 = eye, 0,0,0 = color rgb
    
    behavior_list.do_question_S()
    text_to_speech(f"안녕! 나는 금쪽이라고 해! 너는 이름이 뭐야?")
    #user_name = input("답변 (이름): ")
    time.sleep(3)
    text_to_speech(f"그렇구나 만나서 반가워!")
    
    print(f"user name: {user_name}\n")
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

        if parse == 'positive':
            happydef = [heart_scenario, takepic1, takepic2, happySong]
            # ran = random.randrange(0,4) # 0이상 4미만의 난수
            # print(ran)
            # print(happydef[ran])
            ran = random.choice(happydef)
            ran()
            break
        
        elif parse == 'neutral':
            normaldef = [soso_scenario, soso_takepic]
            # ran = random.randrange(0,2) # 0이상 2미만의 난수
            # print(ran)
            # print(happydef[ran])
            # happydef[ran]()

            ran = random.choice(normaldef)
            ran()
            break

        else:
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
    

Start()

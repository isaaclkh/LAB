import speech_recognition as sr
import string
import random
import time
import sys
import os
import re

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))))

# python module
from src.NLP import NLP, Dictionary
from src.data import behavior_list
from speech_to_text import speech_to_text
from text_to_speech import TextToSpeech

from openpibo.oled import Oled
from openpibo.audio import Audio
from openpibo.motion import Motion
from openpibo.device import Device
from openpibo.vision import Camera

NLP = NLP()
Dic = Dictionary()
tts = TextToSpeech()

r = sr.Recognizer()
r.energy_threshold = 300
mic = sr.Microphone()

def text_to_speech(text):
    filename = "tts.wav"
    print("\n" + text + "\n")
    # tts 파일 생성 (*break time: 문장 간 쉬는 시간)
    tts.tts_connection(text, filename)
    tts.play(filename, 'local', '-1500', False)     # tts 파일 재생

def wait_for(item):
    while True:
        print(f"{item} 기다리는 중")
        break

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

def Start(name):
    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav", out='local', volume=-1000, background=False)

    text_to_speech(f"{name}{aa(name)} 오늘 기분은 어때?")

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
            
        # TODO : 현재 pibo 홈페이지 접속 불가로 감정 분류는 하지 못함 일단 사용자의 답변을 기다리는 것까지
        # stt 결과 처리 (NLP.py 참고)
        answer = NLP.nlp_answer(user_said=text, dic=Dic)

        if answer == 'DONE':
            while True:
                time.sleep(1)
                text_to_speech("아..괜찮아? 무슨 일인지 말해줄 수 있어?")
                break
        else:
            wait_for('DONE')    # DONE 답변 들어올 때까지 stt open 반복
            continue
        break

    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav", out='local', volume=-1000, background=False)

def Cam():
    text_to_speech("너가 기분이 좋으니가 나도 기분이 좋다~! 웃는 모습을 담고 싶은데 우리 사진 찍을래?")

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

        if answer == 'DONE':
            o = Camera()
            # Capture / Read file
            # 이미지 촬영
            img = o.read()
            #img = cam.imread("/home/pi/test.jpg")
            tts.play(filename="/home/pi/AI_pibo2/src/data/audio/사진기소리.mp3",
                    out='local', volume=-1000, background=False)

            # Write(test.jpg라는 이름을 촬영한 이미지 저장)
            o.imwrite("test.jpg", img)
            img = o.convert_img(img, 128, 64)
            p = Oled()
            p.draw_data(img)
            p.show()

        else: #DONE이 아니면
            text_to_speech("아하 별로 사진을 찍고 싶지 않구나! 그래 알겠어")

        break

def Dance():
    text_to_speech("너가 기분이 좋으니깐 춤을 추고 싶은걸?")
    text_to_speech("원한다면 너도 같이 추자~!")
    
    #TODO : 노래 하이라이트만 잘라서 재생 + 모션 제작

def Heart(name):
    text_to_speech(f"{name}{aa(name)} 너가 좋아하니 내가 너무 신나!! 내 심장소리 들려?")

    #TODO : 심장 소리 wav 또는 mp3 파일 저장 + 재생
    
    p = Oled()
    p.draw_image('/home/pi/AI_pibo2/src/data/icon/화면_default1.png')
    p.show()

    text_to_speech(f"안들린다면 내 가슴쪽을 봐줘!! 내 심장이 너무 빨리 뛰어!! 짐심으로 기뻐{name}{aa(name)}")

def Sing(name):
    text_to_speech(f"{name}{aa(name)} 너무 좋은 일이잖아!! 내가 신나는 노래 한 곡 뽑아볼게!")

    #TODO :  랜덤 플레이 리스트


def Cam2(name):
    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav", out='local', volume=-1000, background=False)
    
    text_to_speech("그렇구나 기분 너무 좋겠다! 너가 지금 느끼는 것을 몸으로 표현해줘!")

    os.sleep(10)
    text_to_speech("지금 너무 행복해보인다! 내가 사진에 담아줄게! 그 자세로 있어주면 내가 사진을 찍어줄게!")
    
    o = Camera()
    # Capture / Read file
    # 이미지 촬영
    img = o.read()
    #img = cam.imread("/home/pi/test.jpg")
    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/사진기소리.mp3",
            out='local', volume=-1000, background=False)

    # Write(test.jpg라는 이름을 촬영한 이미지 저장)
    o.imwrite("test.jpg", img)
    img = o.convert_img(img, 128, 64)
    p = Oled()
    p.draw_data(img)
    p.show()

    text_to_speech(f"너무 보기 좋아 {name}{aa(name)}! 내가 이따가 사진 보내줄게")

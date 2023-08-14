import time
from src.textFinal import text_to_speech, stt, tsst
from src.NLP import NLP, Dictionary
from src.text_to_speech import TextToSpeech
from src.activity.music_get import YoutubeAudioDownload
from src.data import behavior_list
from datetime import datetime
import src.data.oled_list as oled
from threading import Thread

from openpibo.motion import Motion

NLP = NLP()
Dic = Dictionary()
audio = TextToSpeech()
m = Motion()
m.set_profile("/home/pi/PCAP/src/data/motion_db.json")

global uAns
global fileN

def songplay():
    global fileN
    audio.play(filename=fileN, out='local', volume=-4000, background=False)

def sadsong() :
    behavior_list.do_question_S("나는 기분이 안좋을 때 노래를 듣는데 혹시 노래 듣는거 좋아해?")
    ans = stt()
    oled.o_heart()
    if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES' :
        text_to_speech("어떤 장르 좋아해? 팝송? 인디? 발라드? 아니면 힙합?")
        mus = stt()
        
        if '힙합' in mus:
            mus = '힙합'
        if '팝송' in mus:
            mus = '팝송'
        if '락' in mus:
            mus = '락'
        if '케이팝' in mus:
            mus = '케이팝'
        if '제이팝' in mus:
            mus = '제이팝'
        if '인디' in mus:
            mus = '인디'
        if '발라드' in mus:
            mus = '발라드'

        if NLP.nlp_answer(user_said=ans, dic=Dic) == 'NO':
            text_to_speech("그럼 내가 노래 하나 추천해 줄까?")
        else : 
            text_to_speech(f"그렇구나! 나도 {mus} 좋아해! 내가 노래 하나 추천해줄까?")
        
        ans = stt()

        if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES' :
            text_to_speech("알겠어, 잠깐만 기다려줘.")

            fileN = YoutubeAudioDownload(f'슬픈{mus}')

            if fileN is "CANNOT":
                text_to_speech("미안, 너가 원하는 노래를 검색했는데, 틀 수 있는게 없어.")
            else :
                audio.play(filename=fileN, out='local', volume=-1000, background=False)

            text_to_speech("이 노래로 위로가 됐으면 하는데, 어땠어?")
            
            ans = stt()
            if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES':
                behavior_list.do_joy("너가 좋다니 다행이다, 다음에도 내가 좋은 노래 많이 추천해줄게.")

            else :
                behavior_list.do_sad("미안해, 다음에는 좋은 노래를 추천해줄게.")
        else :
            text_to_speech("알겠어, 그럼 노래를 틀지 않을게.")
    else :
        text_to_speech("그렇구나.")

def medi() :
    behavior_list.do_question_S("마음을 가다듬고 눈을 감고 내가 들려주는 노래에 맞춰서 호흡을 가다듬어볼래? 너의 복잡한 감정들이 조금은 정리될 수 있도록 도움이 될 거야.")
    #TODO : 명상 틀어주기
    #숨쉬는 동작
    oled.o_nature()
    behavior_list.do_medi()

    text_to_speech("명상하고나니 기분은 좀 어때?")
    ans = stt()

    if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES' :
        behavior_list.do_joy("너가 좋다니 다행이다! 다음에도 나랑 명상하자.")

    else :
        behavior_list.do_sad("이런.. 다음에는 더 좋은 활동을 해보자.")

def drawing() :
    behavior_list.do_question_S("너는 일기 쓰는 거 좋아해?")

    time.sleep(2)
    oled.o_heart()
    text_to_speech("그렇구나. 내가 찾아보니깐, 그림 일기를 썼을 때, 안정감을 찾는다고 해.")
    text_to_speech("그림일기를 한번 그려볼래?")

    ans = stt()

    if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES' :
        text_to_speech("너 앞에 있는 빈종이에, 오늘 있었던 일을 그려줘. 다 그렸으면 다 그렸다고 말해줘.")
        
        oled.o_time()

        while True:
            ans = tsst()
        
            if NLP.nlp_answer(user_said=ans, dic=Dic) == 'DONE':
                break
        
        text_to_speech("다 끝났어? 너의 그림일기를 보고 싶은데, 종이를 들어서 나에게 보여줄래?")
        m.set_motion("scan", 1)
        text_to_speech("정말 잘 그렸다. 무슨 내용이야?")

        time.sleep(10)

        text_to_speech("그렇구나! 그림으로 정말 잘 표현한 것 같아. 그림 일기를 그려보니 어때? 마음이 편안해 진 것 같아?")

        ans = stt()

        if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES' :
            behavior_list.do_joy("다행이다. 나도 일기를 쓰면 마음이 편해지더라고. 앞으로 너도 일기 꾸준히 써봐.")

        else :
            behavior_list.do_sad("저런. 일기 쓰는것이 별로였구나.")


    else :
        text_to_speech("알겠어.")

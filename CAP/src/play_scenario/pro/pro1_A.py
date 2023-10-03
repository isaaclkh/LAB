# -*- coding: utf-8 -*-
#!/usr/bin/python3
# cognition: 인지/지각/사고

# python module

import os
import sys
import time
import re

# openpibo module
import openpibo

# my module
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(
    os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))))
# print(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))))
# from speech_to_text import speech_to_text

from text_to_speech import TextToSpeech
from src.data import oled_list
from src.data import behavior_list
from src.NLP import NLP, Dictionary

NLP = NLP()
Dic = Dictionary()
tts = TextToSpeech()


def text_to_speech(text):
    filename = "tts.wav"
    print("\n" + text + "\n")
    tts.tts_connection(text, filename)
    tts.play(filename, 'local', '-1500', False)


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


def Project_A(user_name):
    print(f"user name: {user_name} \n")

    while True:
        time.sleep(1)
        behavior_list.do_explain_A()
        text_to_speech(
            f"{user_name}{aa(user_name)} 만나서 반가워! 나는 인간에게 다양한 서비스를 제공하기 위해서 만들어진 서비스 로봇이야. 지금부터 내가 무엇을 할 수 있는지 설명해줄게.")
        text_to_speech("나는 반려로봇으로 개발 되었고 휴먼 로봇 인터렉션 연구에 적용되어 사용되고 있어")
        text_to_speech(
            "나는 서버와 통신하며 주고 받은 정보를 통해 작동돼. 그런데 처리해야 할 데이터 연산량이 많기 때문에 내가 직접 처리 하지 않고 카메라에서 찍은 사진을 서버에 전송해서 데이터를 처리하고 있어.")
        text_to_speech(
            "나는 사람 얼굴도 인식할 수 있는데, 인공지능 모델을 이용해서 마스크를 쓴 사람과 쓰지 않은 사람을 구분할 수 있어. 내가 가지고 있는 카메라로 사람의 얼굴을 인식해서 따라다닐 수도 있단다.")
        text_to_speech(
            "그리고 사람의 얼굴을 보고 눈을 맞출 수 있어. 눈맞춤을 하기 위해서 여러분의 얼굴에서 눈의 좌표를 구해 내 목에 있는 모터를 이용해서 목을 움직여. 자연스러운 목 움직임을 위해 모터를 부드럽게 제어할 수도 있어.")
        text_to_speech(
            "지금 여기 있는 모든 사람들과 눈을 맞출 수도 있어. 여러 사람과 눈을 맞추기 위해서 나와 가장 가까이에 있는 사람과 눈맞춤을 하거나 여러 사람들을 일정한 시간 간격으로 랜덤하게 선택해서 여러 사람과 눈을 맞출 수 있어.")
        text_to_speech(
            f"그리고 나는 {user_name}{lee(user_name)}와 대화도 할 수 있어. 먼저, {user_name}{lee(user_name)}의 음성을 듣고 너의 말을 텍스트로 바꿔. 그 뒤에  특정 단어를 인식해 알맞은 대답을 골라 답변할 수 있어. 그리고 대화하는 사람의 수에 따라 대화 볼륨도 조절할 수 있단다. 지금까지 내 소개를 했는데 어땠어?")
        time.sleep(3)
        break

    while True:
        behavior_list.do_question_S()
        text_to_speech(
            f"내 얘기를 끝까지 들어줘서 고마워. {user_name}{lee(user_name)}를 위해서 선물을 하나 준비했는데, 두 가지 종류의 스티커를 준비했어! {user_name}{lee(user_name)}는 무엇을 가져갈래? 고른 후에 나한테 보여줘.")
        user_said = input("답변 (귀여운/멋있는): ")
        oled_list.o_compliment()
        if user_said == '멋있는':
            while True:
                time.sleep(1)
                # 유저가 무엇을 선택했는지 기록
                text_to_speech(
                    f"{user_name}{lee(user_name)}는 멋있는 스티커를 좋아하는구나. 좋은 선택이야!")
                break
        else:
            while True:
                time.sleep(1)
                text_to_speech(
                    f"{user_name}{lee(user_name)}는 귀여운 스티커를 좋아하는구나. 좋은 선택이야!")
                break
        break

    while True:
        text_to_speech("오늘 만나서 반가웠어. 잘가!")
        break


def Play_Project():
    behavior_list.do_question_S()
    text_to_speech("안녕! 내 이름은 파이보야. 너의 이름은 뭐니?")

    user_said = input("답변 (이름): ")
    Project_A(user_said)


Play_Project()

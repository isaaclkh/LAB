#!/usr/bin/python3
# cognition: 인지/지각/사고
import os
import sys
import time
import re

# openpibo module
import openpibo

# my module
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(
    os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))))
print(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(
    os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))))
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


def has_badchim(word):
    m = re.search("[가-힣]+", word)
    if m:
        k = m.group()[-1]
        return (ord(k) - ord("가")) % 28 > 0
    else:
        return


def lee(word):
    josa = "이" if has_badchim(word) else ""
    print(f"{word}{josa} ", end='')
    return josa


def aa(word):
    josa = "아" if has_badchim(word) else "야"
    print(f"{word}{josa} ", end='')
    return josa


def Project_A(user_name, lastcho):
    print(f"user name: {user_name} \n")

    while True:
        time.sleep(1)
        text_to_speech(
            f"안녕 {user_name}{aa(user_name)}. 다시 만나게 되서 반가워!! 오늘은 너의 이야기를 들어주는 서비스를 보여줄거야. 자, 최근에 있었던 일 중에서 기억에 남는 일이 있으면 나에게 이야기해 주겠니?")
        text_to_speech(
            f"앞에 있는 그림 일기에 다가 오늘 {user_name}{lee(user_name)}의 하루는 어땠는지 그림으로 표현해줘. 그리고 그림을 다 그린 후에 나한테 보여줘.")
        break

    while True:
        user_said = input("답변(끝): ")
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'DONE':
            while True:
                time.sleep(1)
                text_to_speech("우와! 혹시 그림 일기에 대해서 설명해 줄 수 있어? ")
                break
        else:
            wait_for('DONE')
            continue
        break

    while True:
        user_said = input("답변 (끝): ")
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'DONE':
            while True:
                time.sleep(1)
                text_to_speech(f"아, 그런 일이 있었구나. {user_name}{lee(user_name)}에 대해서 조금 더 알게 된 것 같아.")
                break
        else:
            wait_for('DONE')    # DONE 답변 들어올 때까지 stt open 반복
        break

    while True:
        behavior_list.do_question_S()
        
        text_to_speech(f"{user_name}{lee(user_name)}의 일상에 대해서 알려줘서 고마워. 이번에도 {user_name}{lee(user_name)}를 위해서 선물을 하나 준비했는데, 두 가지 종류의 스티커를 준비했어. {user_name}{lee(user_name)}는 지난번에 {lastcho} 스티커를 가져갔었는데 이번엔 무엇을 가져갈래? 고른 후에 나한테 보여줘")
        user_said = input("답변(귀여운/멋있는): ")
        oled_list.o_compliment()
        if user_said == '귀여운':
            if user_said == lastcho:
                while True:
                    time.sleep(1)
                    text_to_speech(
                        f"이번에도 귀여운 스티커를 골랐네. {user_name}{lee(user_name)}는 귀여운 스티커를 좋아하는 것 같아")
                    break
            else:
                while True:
                    time.sleep(1)
                    text_to_speech(
                        f"이번에는 귀여운 스티커를 골랐네. {user_name}{lee(user_name)}도 귀여운 스티커를 좋아하는구나")
                    break
        else:
            if lastcho == '귀여운':
                while True:
                    time.sleep(1)
                    text_to_speech(
                        f"이번에는 멋있는 스티커를 골랐네. {user_name}{lee(user_name)}도 멋있는 스티커를 좋아하는구나")
                    break
            else:
                while True:
                    time.sleep(1)
                    text_to_speech(
                        f"이번에도 멋있는 스티커를 골랐네. {user_name}{lee(user_name)}는 멋있는 스티커를 좋아하는 것 같아")
                    break
        break

    while True:
        text_to_speech("오늘 만나서 반가웠어. 잘가!")
        break


def Play_Project():
    user_said = input("이름: ")
    lastchoice = input("저번 선택 (귀여운/멋있는): ")
    Project_A(user_said, lastchoice)


Play_Project()

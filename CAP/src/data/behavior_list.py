# behavior = motion + eye + oled + sound

# python module
import os
import sys
import time
import json
from threading import Thread

# openpibo module
import openpibo
from openpibo.motion import Motion
from openpibo.device import Device
from openpibo.oled import Oled

# my module
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
import src.data.eye_list as eye
import src.data.oled_list as oled
from text_to_speech import TextToSpeech

motion = Motion()
audio = TextToSpeech()

motion.set_profile("/home/pi/AI_pibo2/src/data/motion_db.json")
# 효과음 중 스탬프 찍기, 사진 찍기는 TTS 끝나고 재생 => 놀이 스크립트에서 효과음 재생!

def do_question_L():
    """
    Multi Thread: 병렬 실행을 위해 사용
    ex_1. Thread motion, Thread oled ==> motion + oled 동시 실행
    ex_2. Thread(target=<어디 스크립트.어느 함수>, args=(있으면))
    """
    audio.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav", out='local', volume=-1000, background=False)
    m = Thread(target=motion.set_motion, args=("m_question_L", 1))      # "동작 이름", n번 반복
    o = Thread(target=oled.o_question(), args=())

    m.daemon = True
    o.daemon = True

    m.start()
    o.start()

    while True:
        eye.e_question()  # motion, oled 돌아가는 동안 eyes on
        break


def do_question_S():
    audio.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav", out='local', volume=-1000, background=False)
    m = Thread(target=motion.set_motion, args=("m_question_S", 1))
    o = Thread(target=oled.o_question(), args=())

    m.daemon = True
    o.daemon = True

    m.start()
    o.start()

    while True:
        eye.e_question()
        break


def do_suggestion_L():
    m = Thread(target=motion.set_motion, args=("m_suggestion_L", 1))
    o = Thread(target=oled.o_suggestion, args=())

    m.daemon = True
    o.daemon = True

    m.start()
    o.start()

    while True:
        eye.e_suggestion()
        break


def do_suggestion_S():
    m = Thread(target=motion.set_motion, args=("m_suggestion_S", 1))
    o = Thread(target=oled.o_suggestion, args=())

    m.daemon = True
    o.daemon = True

    m.start()
    o.start()

    while True:
        eye.e_suggestion()
        break


def do_explain_A():
    m = Thread(target=motion.set_motion, args=("m_explain_A", 1))
    o = Thread(target=oled.o_explain, args=())

    m.daemon = True
    o.daemon = True

    m.start()
    o.start()

    while True:
        eye.e_explain()
        break


def do_explain_B():
    m = Thread(target=motion.set_motion, args=("m_explain_B", 1))
    o = Thread(target=oled.o_explain, args=())

    m.daemon = True
    o.daemon = True

    m.start()
    o.start()

    while True:
        eye.e_explain()
        break


def do_photo():
    m = Thread(target=motion.set_motion, args=("m_photo", 1))
    o = Thread(target=oled.o_photo, args=())

    m.daemon = True
    o.daemon = True

    m.start()
    o.start()

    while True:
        eye.e_photo()
        break


def do_stamp():
    m = Thread(target=motion.set_motion, args=("m_stamp", 1))
    o = Thread(target=oled.o_stamp, args=())

    m.daemon = True
    o.daemon = True

    m.start()
    o.start()

    while True:
        eye.e_stamp()
        break


def do_waiting_A():
    m = Thread(target=motion.set_motion, args=("m_waiting_A", 1))
    o = Thread(target=oled.o_waiting(), args=())

    m.daemon = True
    o.daemon = True

    m.start()
    o.start()

    while True:
        eye.e_waiting()
        break


def do_waiting_B():
    m = Thread(target=motion.set_motion, args=("m_waiting_B", 1))
    o = Thread(target=oled.o_waiting(), args=())

    m.daemon = True
    o.daemon = True

    m.start()
    o.start()

    while True:
        eye.e_waiting()
        break


def do_waiting_C():
    m = Thread(target=motion.set_motion, args=("m_waiting_C", 1))
    o = Thread(target=oled.o_waiting(), args=())

    m.daemon = True
    o.daemon = True

    m.start()
    o.start()

    while True:
        eye.e_waiting()
        break


def do_praise_L():
    audio.play(filename="/home/pi/AI_pibo2/src/data/audio/경쾌한음악.wav", out='local', volume=-1000, background=False)
    m = Thread(target=motion.set_motion, args=("m_praise_L", 1))
    o = Thread(target=oled.o_compliment, args=())

    m.daemon = True
    o.daemon = True

    m.start()
    o.start()

    while True:
        eye.e_praise()
        break


def do_praise_S():
    audio.play(filename="/home/pi/AI_pibo2/src/data/audio/경쾌한음악.wav", out='local', volume=-1000, background=False)
    m = Thread(target=motion.set_motion, args=("m_praise_S", 1))
    o = Thread(target=oled.o_compliment, args=())

    m.daemon = True
    o.daemon = True

    m.start()
    o.start()

    while True:
        eye.e_praise()
        break


def do_agree():
    audio.play(filename="/home/pi/AI_pibo2/src/data/audio/딩동댕3.wav", out='local', volume=-1000, background=False)
    m = Thread(target=motion.set_motion, args=("m_agree", 1))
    o = Thread(target=oled.o_agree(), args=())

    m.daemon = True
    o.daemon = True

    m.start()
    o.start()

    while True:
        eye.e_agree()
        break


def do_joy():
    audio.play(filename="/home/pi/AI_pibo2/src/data/audio/기분좋음.mp3", out='local', volume=-1000, background=False)
    m = Thread(target=motion.set_motion, args=("m_joy", 1))
    o = Thread(target=oled.o_joy(), args=())

    m.daemon = True
    o.daemon = True

    m.start()
    o.start()

    while True:
        eye.e_joy()
        break


def do_sad():
    audio.play(filename="/home/pi/AI_pibo2/src/data/audio/슬픈소리.wav", out='local', volume=-1000, background=False)
    m = Thread(target=motion.set_motion, args=("m_sad", 1))
    o = Thread(target=oled.o_sad(), args=())

    m.daemon = True
    o.daemon = True

    m.start()
    o.start()

    while True:
        eye.e_sad()
        break


def praising():
    m = Thread(target=motion.set_motion, args=("m_praise_S", 1))
    o = Thread(target=oled.o_cheer, args=())

    m.daemon = True
    o.daemon = True

    m.start()
    o.start()

    while True:
        eye.e_praise()
        break


def heart():
    m = Thread(target=motion.set_motion, args=("m_sad", 1))
    o = Thread(target=oled.o_sad, args=())

    m.daemon = True
    o.daemon = True

    m.start()
    o.start()

    while True:
        eye.e_praise()
        break


def touch():
    m = Thread(target=motion.set_motion, args=("m_sad", 1))
    o = Thread(target=oled.o_search, args=())

    m.daemon = True
    o.daemon = True

    m.start()
    o.start()


def neutral():
    audio.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav",
               out='local', volume=-1000, background=False)
    m = Thread(target=motion.set_motion, args=("m_sad", 1))
    o = Thread(target=oled.o_neutral, args=())

    m.daemon = True
    o.daemon = True

    m.start()
    o.start()

    while True:
        eye.e_sad()
        break

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

NLP = NLP()
Dic = Dictionary()
device_obj = Device()
camera = Camera()
oled = Oled()
tts = TextToSpeech()

m = Motion()
m.set_profile("/home/pi/PCAP/src/data/motion_db.json")

# behavior_list.do_positivie_dance()
# # text_to_speech("자 드가자. 고고고고고고고고고")

behavior_list.do_positivie_dance()
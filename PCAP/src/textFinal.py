import speech_recognition as sr
from src.text_to_speech import TextToSpeech
import src.data.oled_list as oled

mic = sr.Microphone()
tts = TextToSpeech()

r = sr.Recognizer()
r.energy_threshold = 300

def text_to_speech(text):
    # sendTo(text)
    filename = "tts.wav"
    print("\n" + text + "\n")
    # tts 파일 생성 (*break time: 문장 간 쉬는 시간)
    tts.tts_connection(text, filename)
    tts.play(filename, 'local', '-1000', False)     # tts 파일 재생

def text_to_speech2(text):  # 원탁 아저씨
    # sendTo(text)
    filename = "tts.wav"
    print("\n" + text + "\n")
    # tts 파일 생성 (*break time: 문장 간 쉬는 시간)
    tts.tts_connection2(text, filename)
    tts.play(filename, 'local', '-1000', False)     # tts 파일 재생

def stt() : 
    while True:
        with mic as source:
            print("say something\n")
            oled.o_get()
            audio = r.listen(source, timeout=0, phrase_time_limit=5)
            try:
                text = r.recognize_google(audio_data=audio, language="ko-KR")
                oled.o_agree()
                return text
            except sr.UnknownValueError:
                print("say again plz\n")
                oled.o_cannot()
                text_to_speech('잘, 못 알아들었어. 다시 말해줄래?')
                continue
            except sr.RequestError:
                print("speech service down\n")
                continue

def lstt() : 
    while True:
        with mic as source:
            oled.o_get()
            print("say something\n")
            audio = r.listen(source, timeout=0, phrase_time_limit=10)
            try:
                text = r.recognize_google(audio_data=audio, language="ko-KR")
                return text
            except sr.UnknownValueError:
                print("say again plz\n")
                oled.o_cannot()
                text_to_speech('잘, 못 알아들었어. 다시 말해줄래?')
                continue
            except sr.RequestError:
                print("speech service down\n")
                continue

def tsst() : 
    while True:
        with mic as source:
            print("say something\n")
            audio = r.listen(source, timeout=0, phrase_time_limit=5)
            try:
                text = r.recognize_google(audio_data=audio, language="ko-KR")
                return text
            except sr.UnknownValueError:
                print("say again plz\n")
                continue
            except sr.RequestError:
                print("speech service down\n")
                continue
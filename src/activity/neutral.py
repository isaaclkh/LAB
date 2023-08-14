import time
from src.textFinal import text_to_speech, stt, tsst
from src.NLP import NLP, Dictionary
from src.text_to_speech import TextToSpeech
from src.activity.music_get import YoutubeAudioDownload
from src.data import behavior_list
from datetime import datetime
import src.data.oled_list as oled
from threading import Thread


NLP = NLP()
Dic = Dictionary()
audio = TextToSpeech()

global uAns
global fileN

def songplay():
    global fileN
    audio.play(filename=fileN, out='local', volume=-4000, background=False)

def midsong() :
    behavior_list.do_question_S("나는 노래 듣고 부르는 걸 좋아하는데 너는 노래 듣는거 좋아해?")
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

            fileN = YoutubeAudioDownload(mus)

            if fileN is "CANNOT":
                text_to_speech("미안, 너가 원하는 노래를 검색했는데, 틀 수 있는게 없어.")
            else :
                audio.play(filename=fileN, out='local', volume=-1000, background=False)

            text_to_speech("내 추천 곡 어땠어?")
            
            ans = stt()
            if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES':
                behavior_list.do_joy("좋아해주니 나도 기분이 좋다. 다음에도 좋은 노래 추천해줄게.")
            else :
                behavior_list.do_sad("미안해, 다음에는 좋은 노래를 추천해줄게")
        else :
            text_to_speech("알겠어, 그럼 노래를 틀지 않을게.")
    
    else:
        text_to_speech("그렇구나.")

def midtalk():
    behavior_list.do_question_S("나랑 게임 하나 해볼래?")

    ans = stt()

    oled.o_heart()

    if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES':
        text_to_speech("좋아! 거짓과 진실이라는 게임인데, 내가 진실 두개, 거짓 하나를 말할거야.")
        text_to_speech("그 중에서 내가 거짓말을 한 것을 맞춰봐!")
        time.sleep(1)
        text_to_speech("일번. 나는 팔이 삼백육십도 돌아가지 않는다.")
        audio.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav",
                   out='local', volume=-1000, background=False)
        text_to_speech("이번. 나는 나의 눈 색깔을 바꿀 수 있다.")
        audio.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav",
                   out='local', volume=-1000, background=False)
        text_to_speech("삼번. 나는 내눈을 통해서 너를 볼 수 있다.")
        audio.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav",
                   out='local', volume=-1000, background=False)
        
        text_to_speech("자, 이제 맞춰봐. 띠링 소리 이후에 일번, 이번, 삼번 이라고 얘기해주면 되.")
        audio.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav",
                   out='local', volume=-1000, background=False)
        
        ans = stt()

        if NLP.nlp_number(user_said=ans, dic=Dic) == '3':
            oled.o_agree()
            behavior_list.do_joy("딩동댕! 맞았어!")
        
        else :
            oled.o_deny()
            behavior_list.do_sad("땡! 틀렸어. 나는 카메라가 입에 있어서 내눈으로는 너를 볼 수 없어. 히히")
        
        text_to_speech("이제 너 차라례야, 10초 동안 준비할 시간을 줄게.")
        
        # TODO : 기다리는 10초 동안 무언가를 보여주는

        oled.o_time()

        time.sleep(10)

        text_to_speech("이제 시작할게. 내 띠링 소리에 맞춰서 하나씩 말해줘.")

        audio.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav",
                   out='local', volume=-1000, background=False)
        one = stt()
        audio.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav",
                   out='local', volume=-1000, background=False)
        two = stt()
        audio.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav",
                   out='local', volume=-1000, background=False)
        three = stt()
        audio.play(filename="/home/pi/AI_pibo2/src/data/audio/물음표소리1.wav",
                   out='local', volume=-1000, background=False)
        
        text_to_speech("이번. 맞았어?")

        ans = stt()

        if NLP.nlp_wrong(user_said=ans, dic=Dic) == 'WRONG' :
            text_to_speech("그래? 그럼 정답은 뭐야?")
            ans = stt()
            text_to_speech("그렇구나!")

        else :
            behavior_list.do_joy(f"아싸! 그럼 {two}가 거짓이구나!")

        text_to_speech("너를 조금 더 알아갈 수 있어서 좋았어. 너는 어뗐어?")
        
        ans = stt()

        if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES':
            behavior_list.do_joy("다행이다! 다음에도 나랑 게임하자")
        
        else :
            behavior_list.do_sad("미안해, 다음에는 더 재미있는걸 준비해 놓을게.")
    
    else :
        text_to_speech("아쉽구먼.")
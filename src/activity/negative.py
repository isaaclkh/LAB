import time
from src.textFinal import text_to_speech, stt, lstt
from src.NLP import NLP, Dictionary
from src.text_to_speech import TextToSpeech
import openpibo
from openpibo.oled import Oled
from src.activity.music_get import YoutubeAudioDownload
from src.data import behavior_list

o = Oled()
NLP = NLP()
Dic = Dictionary()
audio = TextToSpeech()

def sadsong() :
    text_to_speech("나는 기분이 안좋을 때 노래를 듣는데 혹시 노래 듣는거 좋아해?")
    ans = stt()

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
            text_to_speech("그래, 내가 유튜브에서 검색해서 틀어줄게. 그래서 조금 시간이 걸리지만, 잠깐만 기달려줘.")

            fileN = YoutubeAudioDownload(f'슬픈{mus}')

            if fileN is "CANNOT":
                text_to_speech("미안, 너가 원하는 노래를 유튜브에 검색했는데, 틀 수 있는게 없어.")
            else :
                audio.play(filename=fileN, out='local', volume=-2000, background=False)

            text_to_speech("위로가 됐으면 하는데 어땠어?")
            
            ans = stt()
            if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES':
                text_to_speech("너가 좋다니 다행이다, 다음에도 내가 좋은 노래 많이 추천해줄게.")
            else :
                text_to_speech("미안해, 다음에는 좋은 노래를 추천해줄게.")
        else :
            text_to_speech("알겠어, 그럼 노래를 틀지 않을게.")

def medy() :
    text_to_speech("마음을 가다듬고 눈을 감고 내가 들려주는 노래에 맞춰서 호흡을 가다듬어볼래? 너의 복잡한 감정들이 조금은 정리될 수 있도록 도움이 될 거야.")

    #TODO : 명상 틀어주기
    #숨쉬는 동작
    behavior_list.do_breath_long()

    text_to_speech("하고나니 기분은 좀 어때?")
    ans = stt()

    if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES' :
        text_to_speech("너가 좋다니 다행이다~ 다음에도 나랑 명상하자.")

    else :
        text_to_speech("이런.. 다음에는 더 좋은 활동을 해보자.")

def drawing() :
    text_to_speech("요즘 너가 즐겨하는게 뭐가 있어?")

    time.sleep(2)

    text_to_speech("아 그렇구나~ 재밌겠다. 나도 다음에 해봐야지~ 나는 요즘 일기를 쓰는데 재밌더라고, 너는 일기 써?")

    time.sleep(2)

    text_to_speech("그렇구나! 일기가 마음이 정리되는 것에 도움이 된다고하던데, 그림일기 한번 그려볼래?")

    # 그림 어디따 그릴지
    ans = stt()

    if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES' :
        text_to_speech("너 앞에 있는 화면에 오늘 있었던 일 그려줘, 다 그렸으면 끝이라고 말해줘.")
        
        oled.draw_image("/home/pi/AI_pibo2/src/data/icon/화면_시계.png")
        oled.show()

        while True:
            ans = tsst()
        
            if NLP.nlp_answer(user_said=ans, dic=Dic) == 'Done':
                break

        text_to_speech("정말 잘 그렸다. 무슨 내용이야?")

        time.sleep(10)

        text_to_speech("그렇구나! 그림으로 정말 잘 표현한 것 같아. 그림 일기를 그려보니 어때?")

        if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES' :
            text_to_speech("다행이다. 나는 일기를 쓰면 마음이 편해지고 기억에 남는 일들을 기록하며 성장하는 느낌이 들더라고. 앞으로 너도 일기 꾸준히 써봐.")

        else :
            text_to_speech("이런. 일기 쓰는것이 별로였구나. 다음엔 다른 활동 하자.")


    else :
        text_to_speech("알겠어, 일기 그리고 싶지 않구나.")

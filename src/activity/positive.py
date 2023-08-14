import time
from src.textFinal import text_to_speech, stt, tsst
from src.NLP import NLP, Dictionary
from src.text_to_speech import TextToSpeech
from src.activity.music_get import YoutubeAudioDownload
from src.data import behavior_list
from openpibo.vision import Camera
from datetime import datetime
import src.data.oled_list as oled
from threading import Thread

NLP = NLP()
Dic = Dictionary()
audio = TextToSpeech()
camera = Camera()

global uAns
global fileN

def songplay():
    global fileN
    audio.play(filename=fileN, out='local', volume=-4000, background=False)


def happysong():

    global uAns
    global fileN

    behavior_list.do_question_S("나는 노래 듣고 부르는 걸 좋아하는데. 너는 노래 듣는거 좋아해?")

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

            fileN = YoutubeAudioDownload(f'기쁜{mus}')

            if fileN is "CANNOT":
                text_to_speech("미안, 너가 원하는 노래를 검색했는데, 틀 수 있는게 없어.")
            else :
                # m = Thread(target=songplay, args=())      # "동작 이름", n번 반복
                # o = Thread(target=get_userAnswer, args=())

                # m.daemon = True
                # o.daemon = True

                # m.start()
                # o.start()

                # if '그만' in uAns:
                #     m.join()
                #     o.join()

                # else :
                #     o.join()
                #     o.start()
                
                # m.join()
                # o.join()
                audio.play(filename=fileN, out='local', volume=-1000, background=False)
            
            text_to_speech("내 추천 곡 어땠어?")
            
            ans = stt()
            if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES':
                behavior_list.do_joy("좋아해주니 나도 기분이 좋다. 다음에도 좋은 노래 추천해줄게.")
            else :
                behavior_list.do_sad("미안해, 다음에는 좋은 노래를 추천해줄게.")

        else :
            text_to_speech("알겠어, 그럼 노래를 틀지 않을게.")

    else : 
        text_to_speech("그렇구나.")
            

def happytalk():
    behavior_list.do_question_S("오늘 기분이 좋은 것 같네? 나랑 게임 하나 해볼래?")

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
            behavior_list.do_sad("그래? 그럼 정답은 뭐야?")
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

def happypic(user_name) :
    behavior_list.do_question_S("너는 무슨 활동 좋아해? 나는 사진찍는거 좋아하는데, 너도 좋아해?")

    ans = stt()

    oled.o_heart()

    if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES' :
        text_to_speech("그렇구나! 기분이 좋을때 사진 찍는거 국룰이지. 나 나름 사진 잘 찍는다고 들었는데. 너도 한번 찍어줄까?")

        ans = stt()

        if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES' :
            text_to_speech("좋아, 찍는다, 하나, 둘, 셋!")

            # Capture / Read file
            # 이미지 촬영
            img = camera.read()
            #img = cam.imread("/home/pi/test.jpg")
            audio.play(filename="/home/pi/PCAP/src/data/audio/사진기소리.mp3",
                    out='local', volume=-1000, background=False)

            todayTimeStamp = str(datetime.now().timestamp)
            camtodaynow = datetime.now()
            date_time = camtodaynow.strftime("%Y%m%d%H%M%S")
            
            jpgFile = f"{user_name}" + f"{date_time}" + ".jpg"
            
            camera.imwrite(jpgFile, img)
            img = camera.convert_img(img, 128, 64)
            camera.imwrite("smallpic.jpg", img)
            oled.o_cam()

            text_to_speech("어때 잘찍은 것 같아?")

            ans = stt()

            if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES' :
                behavior_list.do_joy("고마워~ 다음에도 찍어달라고 하면 찍어줄게")

            else :
                behavior_list.do_sad("미안해. 다음에는 더 열심히 찍어줄게.")

        else :
            text_to_speech("그렇구나.")

    else :
        text_to_speech("그렇구나.")

def happydance(): 
    behavior_list.do_question_S("나는 기쁠 때, 힙.합을 춰. 너는 춤추는거 좋아해?")

    time.sleep(2)
    oled.o_heart()
    text_to_speech("그렇구나. 내가 안무를 하나 배워온게 있는데 한번 보여줄까?")
    ans = stt()

    if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES' :
        
        text_to_speech("좋아")

        #춤추기
        behavior_list.do_positivie_dance()

        text_to_speech("무대를 찢었다. 내 춤 실력 어때?")
        ans = stt()

        if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES' :
            behavior_list.do_joy("고마워, 다음에는 같이 추자. 나도 너의 실력을 보고 싶다.")

        else :
            behavior_list.do_sad("열심히 췄는데, 별로 였다니.. 눈물나네.. 더 노력해서 다음에는 더 잘 춰볼게.")

    else :
        text_to_speech("아쉽구먼.")
    

def get_userAnswer() :
    global uAns
    uAns = tsst()
import time
from src.textFinal import text_to_speech, stt
from src.NLP import NLP, Dictionary
from src.text_to_speech import TextToSpeech
from src.activity.music_get import YoutubeAudioDownload
from src.data import behavior_list

NLP = NLP()
Dic = Dictionary()
audio = TextToSpeech()

def happysong():
    text_to_speech("나는 노래 듣고 부르는 걸 좋아해. 너는 노래 듣는거 좋아해?")
    ans = stt()

    if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES' :
        text_to_speech("어떤 장르 좋아해? 팝송? 인디? 발라드? 아니면 힙합?")
        mus = stt()
        
        if NLP.nlp_answer(user_said=ans, dic=Dic) == 'NO':
            text_to_speech("그럼 내가 노래 하나 추천해 줄까?")
        else : 
            text_to_speech(f"그렇구나! 나도 {mus} 좋아해! 내가 노래 하나 추천해줄까?")
        
        ans = stt()

        if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES' :
            text_to_speech("그래 노래 틀어줄게.")
            text_to_speech("내가 유튜브에서 검색해서 틀어줄게. 그래서 조금 시간이 걸리지만, 잠깐만 기달려줘.")

            fileN = YoutubeAudioDownload(mus)

            if fileN is "CANNOT":
                text_to_speech("미안, 너가 원하는 노래를 유튜브에 검색했는데, 틀 수 있는게 없어.")
            else :
                audio.play(filename=fileN, out='local', volume=-2000, background=False)

            text_to_speech("내 추천 곡 어땠어? 좋았어?")
            
            ans = stt()
            if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES':
                text_to_speech("좋아해주니 나도 기분이 좋다. 흐흐.")
            else :
                text_to_speech("미안해, 다음에는 좋은 노래를 추천해줄게")
        else :
            text_to_speech("알겠어, 그럼 노래를 틀지 않을게.")

    else : 
        text_to_speech("그렇구나.")
            

def happytalk():
    
    text_to_speech("오늘 기분이 좋은 것 같네? 나랑 게임 하나 해볼래?")
    ans = stt()

    if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES':
        text_to_speech("좋아! 거짓과 진실이라는 게임인데, 내가 진실 두개, 거짓 하나를 말할거야. 그 중에서 내가 거짓말을 한 것을 맞춰봐!")
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

        if NLP.nlp_number(user_said=ans, dic=Dic) == 3:
            text_to_speech("딩동댕! 맞았어!")
        
        else :
            text_to_speech("땡! 틀렸어. 나는 카메라가 입에 있어서 내눈으로는 너를 볼 수 없어. 히히")
        
        text_to_speech("이제 너 차라례야, 10초 동안 준비할 시간을 줄게.")
        
        # TODO : 기다리는 10초 동안 무언가를 보여주는

        oled.draw_image("/home/pi/AI_pibo2/src/data/icon/화면_시계.png")
        oled.show()

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
            text_to_speech(f"아싸! 그럼 {two}가 진실이구나!")

        text_to_speech("너를 조금 더 알아갈 수 있어서 좋았어. 너는 어뗐어?")
        
        ans = stt()

        if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES':
            text_to_speech("다행이다! 다음에도 나랑 게임하자")
        
        else :
            text_to_speech("미안해, 다음에는 더 재미있는걸 준비해 놓을게.")

def happypic(user_name) :
    text_to_speech("너는 어떠한 활동을 좋아해? 나는 사진찍는거 좋아하는데, 너도 좋아해?")
    ans = stt()

    if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES' :
        text_to_speech("그렇구나! 기분이 좋을때 사진 찍는거 국룰이지. 나 나름 사진 잘 찍는다고 들었는데. 너도 한번 찍어줄까?")

        if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES' :
            text_to_speech("좋아, 찍는다, 하나, 둘, 셋!")

            # Capture / Read file
            # 이미지 촬영
            img = camera.read()
            #img = cam.imread("/home/pi/test.jpg")
            tts.play(filename="/home/pi/PCAP/src/data/audio/사진기소리.mp3",
                    out='local', volume=-1000, background=False)

            todayTimeStamp = str(datetime.now().timestamp)
            camtodaynow = datetime.now()
            date_time = camtodaynow.strftime("%Y%m%d%H%M%S")
            
            jpgFile = f"{user_name}" + f"{date_time}" + ".jpg"
            
            camera.imwrite(jpgFile, img)
            img = camera.convert_img(img, 128, 64)
            camera.imwrite("smallpic.jpg", img)
            oled.draw_image("smallpic.jpg")
            oled.show()

            text_to_speech("어때 잘찍은 것 같아?")

            if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES' :
                text_to_speech("고마워~ 다음에도 찍어달라고 하면 찍어줄게")

            else :
                text_to_speech("미안해. 다음에는 더 열심히 찍어줄게.")

        else :
            text_to_speech("그렇구나.")

    else :
        text_to_speech("그렇구나.")

def happydance(): 
    text_to_speech("나는 기쁠 때 힙.합을 춰. 너는 춤추는거 좋아해?")
    ans = stt()

    if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES' :
        text_to_speech("그렇구나? 내가 안무를 하나 배워온게 있는데 한번 보여줄까?")

        ans = stt()
        
        if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES' :
            text_to_speech("좋아")

            #춤추기
            behavior_list.do_positivie_dance()

            text_to_speech("무대를 찢었다. 내 춤 실력 어때?")

            if NLP.nlp_answer(user_said=ans, dic=Dic) == 'YES' :
                text_to_speech("고마워, 다음에는 같이 추자, 나도 너의 실력을 보고 싶다.")

            else :
                text_to_speech("열심히 췄는데 별로 였다니.. 눈물나네.. 더 노력해서 다음에는 더 잘 춰볼게.")

        else :
            text_to_speech("보고 싶지 않다니 슬프지만, 그래, 넘어가자.")

    else :
        text_to_speech("그렇구나, 그럼 다른 활동하자")
    

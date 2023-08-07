from src.textFinal import text_to_speech, stt, lstt
from src.NLP import NLP, Dictionary
from src.text_to_speech import TextToSpeech

def Cam():
    # Capture / Read file
    # 이미지 촬영
    img = camera.read()
    #img = cam.imread("/home/pi/test.jpg")
    tts.play(filename="/home/pi/AI_pibo2/src/data/audio/사진기소리.mp3",
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

    blob = bucket.blob(jpgFile)
    # blob = bucket.blob(f'{user_name}/'+file)
    #new token and metadata 설정
    new_token = uuid4()
    metadata = {"firebaseStorageDownloadTokens": new_token} #access token이 필요하다.
    blob.metadata = metadata

    #upload file
    blob.upload_from_filename(filename=jpgFile, content_type='image/jpeg')
    blob.make_public()
    print(blob.public_url)

    doc_pic = db.collection(u'users').document(f'{user_name}').collection(u'사진').document(f'{date_time}')
    tt = jpgFile.split(".jpg")
    finaltt = tt[0].split(f"{user_name}")
    doc_pic.set({'url' : blob.public_url, 'time' : finaltt[1]})

    os.system("rm %s" %jpgFile)
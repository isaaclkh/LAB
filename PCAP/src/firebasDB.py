import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from uuid import uuid4
from firebase_admin import storage

# 서비스 계정의 비공개 키 파일이름
cred = credentials.Certificate(
    "/home/pi/AI_pibo2/src/play_scenario/CAP/pibo-aac5a-firebase-adminsdk-94r6k-faf630e478.json")
firebase_admin.initialize_app(cred, {
    #gs://pibo-aac5a.appspot.com
    'apiKey': "AIzaSyDF5r0N2u8KVFILABFMCtNbF7w4VtmQy54",
    'authDomain': "pibo-aac5a.firebaseapp.com",
    'databaseURL': "https://pibo-aac5a-default-rtdb.firebaseio.com",
    'projectId': "pibo-aac5a",
    'storageBucket': "pibo-aac5a.appspot.com",
    'messagingSenderId': "516104758418",
    'appId': "1:516104758418:web:81dd90f1624515f8f6f24b"
})
db = firestore.client()
# doc_ref.set({u'느낌' : 'BAD'})
bucket = storage.bucket()  # 기본 버킷 사용


# def sendTo(message):
#     doc_topibo = db.collection(u'connectwithpibo').document('toPibo')
#     doc_frompibo = db.collection(u'connectwithpibo').document('fromPibo')

#     doc_frompibo.set({'msg': message})
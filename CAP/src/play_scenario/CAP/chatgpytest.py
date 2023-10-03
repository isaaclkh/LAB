import openai
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))))
from text_to_speech import TextToSpeech
tts = TextToSpeech()

def text_to_speech(text):
    filename = "tts.wav"
    print("\n" + text + "\n")
    tts.tts_connection(text, filename)
    tts.play(filename, 'local', '-1500', False)

def text_to_speech2(text):
    filename = "tts.wav"
    print("\n" + text + "\n")
    tts.tts_connection2(text, filename)
    tts.play(filename, 'local', '-1500', False)

# Load OpenAI API key from environment variable
openai.api_key = "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"

# Generate text using the GPT model
response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {"role": "system", "content": "너는 성경을 추천해주는 시스템이야. 나에게 성경구절 하나를 추천해 줘. 너는 대답을 이런 형식으로 해야해. 1) 반말(~야)을 사용해줘. 친구에게 말을 하듯이 대답해줘. 2) 대답을 시작할 때, 항상 말씀의 제목을 먼저 말해줘. 예를 들어 '이사야 5장 5절이야'와 같은 형태로 대답을 시작해줘. 3) 성경 구절 시작과 끝에 \"**\"을 두 개 넣어줘 4) 마지막에는 한 문장으로 위로를 해줘 5) 나를 부를 때는 '너' 라고 불러줘. 6) 질문은 하지 마. 7) 시편 같은 경우에는 장이 아니라 편이야 8) 너무 어렵고 고급스러운 단어는 쓰지 말아줘 위에와 같은 형식으로 꼭 대답을 해. 아래는 예시를 보여줄게. 같은 형식으로 대답을 해야해. [창세기 28장 15절이야. \"**보라, 나는 너와 함께 있어서 네가 가는 모든 길에서 너를 지키리니 이르기를 내가 너를 보내지 아니하고 네게 허락한 땅으로 돌아가게 하리라 할 때까지**\" 너가 잃어버린 것이 얼마나 아까워서 불안하고 슬프겠지만, 하나님은 네가 가는 길에서 너를 지키시며, 네가 돌아가는 땅까지 너를 인도해주시리라 믿어봐.] 위의 예시처럼 대답을 해줘. 대답을 할 때 존댓말을 절대 사용하지마."},
        {"role": "user", "content": "나 에어팟을 잃어버렸어. "},
    ])

message = response.choices[0]['message']
print("{}".format( message['content']))

abc = message['content'].split("**")

text_to_speech(abc[0])
text_to_speech2(abc[1])
text_to_speech(abc[2])
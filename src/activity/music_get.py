from pytube import Search
from pytube import YouTube
import pytube
import time
import os

from moviepy.editor import *

# from src.textFinal import text_to_speech, stt
# from src.text_to_speech import TextToSpeech


def YoutubeAudioDownload(keyword):
    s = Search(keyword)
    print(f"url : {s.results[0].watch_url}\n")

    downloadF = "src//music//" + keyword + ".mp3"

    video = YouTube(url = s.results[0].watch_url, use_oauth = True)
    audio = video.streams.filter(only_audio=True).first()

    try:
        out_file = audio.download(filename = downloadF)
        base, ext = os.path.splitext(out_file)
        # new_file = "src//music//" + keyword + '.mp4'
        # os.rename(out_file, new_file)
        return out_file
    except:
        print("Failed to download audio")
        print("An error occurred:", error)
        # text_to_speech("미안, 너가 원하는 노래를 유튜브에 검색했는데, 틀 수 있는게 없어.")
        return "CANNOT"

    # print("audio was downloaded successfully")
    # fname = new_file
    # video = VideoFileClip(fname)
    # newfname = keyword + ".mp3"
    # video.audio.write_adiofile(newfname)
    
    # return newfname
    # tts.play(filename="/home/pi/PCAP/src/music/" + video.title + ".mp4", out='local', volume=-2000, background=False)

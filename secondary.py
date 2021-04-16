from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from gtts import gTTS
import os
from pytube import YouTube
from playsound import playsound
import vlc
import re, requests, subprocess, urllib.parse, urllib.request
from bs4 import BeautifulSoup
import speech_recognition as sr
import os.path
from os import path
import random
import webbrowser
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

os.system("")
chatbot = ChatBot('Cortana')
trainer = ChatterBotCorpusTrainer(chatbot)
authenticator = IAMAuthenticator('API')
text_to_speech = TextToSpeechV1(
        authenticator=authenticator
    )

text_to_speech.set_service_url('URL')

def tts(output):
    print(output)

    with open('text.mp3', 'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(output, voice='en-GB_CharlotteV3Voice',
                                      accept='audio/mp3').get_result().content)

    playsound('text.mp3')
    os.remove("text.mp3")

def moment(text):
    response = chatbot.get_response(text)
    tts(response)

def speak():
    input = sr.Recognizer()
    with sr.Microphone() as source:
        audio = input.listen(source)
        data = ""
        try:
            data = input.recognize_google(audio)
            print("You said:", data)
            response = chatbot.get_response(data)
            speech = gTTS(text=str(response), lang='hi', slow=False)
            print(response)
            speech.save("text.mp3")
            playsound("text.mp3")
            os.remove("text.mp3")
        except:
            pass

    speak()

def error():
    error = 'Request failed'
    speech = gTTS(text=str(error), lang='en', slow=False)
    print(error)
    speech.save("text.mp3")
    playsound("text.mp3")
    os.remove("text.mp3")

def add_to_playlist(text):
    text = text.replace('add song', '')
    text = text.replace('add track', '')
    text = text.replace('playlist', '')

    music_name = text
    query_string = urllib.parse.urlencode({"search_query": music_name})
    formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)

    search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
    clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
    clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])

    inspect = BeautifulSoup(clip.content, "html.parser")
    yt_title = inspect.find_all("meta", property="og:title")

    for concatMusic1 in yt_title:
        pass

    exam_path = r'C:\Users\docto\PycharmProjects\Cortana 2.6\Playlist' + "\\" + concatMusic1["content"] + ".mp3"
    check = path.exists(exam_path)
    song = concatMusic1

    if check:
        tts(f"Track: {concatMusic1['content']} is already in playlist.")
        return "stopped"

    elif not check:
        tts("[Downloading track...]")
        yt = YouTube(str(clip2))

        video = yt.streams.filter(only_audio=True).first()
        destination = str(r'C:\Users\docto\PycharmProjects\Cortana 2.6\Playlist')

        out_file = video.download(output_path=destination)

        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        tts(f"{concatMusic1['content']} has successfully downloaded...")

    return "stopped"

def remove(text, onlyfiles):
    text = text.replace('remove', '')
    music_name = text
    query_string = urllib.parse.urlencode({"search_query": music_name})
    formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)

    search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
    clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
    clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])

    inspect = BeautifulSoup(clip.content, "html.parser")
    yt_title = inspect.find_all("meta", property="og:title")

    for concatMusic1 in yt_title:
        pass

    exam = concatMusic1["content"]
    exam = exam.replace(".", "")
    exam = exam.replace("'", "")
    exam = exam + ".mp3"

    exam_path = r"C:\Users\docto\PycharmProjects\Cortana 2.6\Playlist" + "\\" + exam

    check = False

    for i in onlyfiles:
        i = i.replace(".mp3", "")

        if text in i.lower():
            check = True

    song = concatMusic1

    if check:
        os.remove(exam_path)
        delete = concatMusic1["content"] + " has been deleted from playlist..."
        tts(delete)

    elif not check:
        tts("Track not found...")

def open_app(text):
    if "roblox" in text:
        webbrowser.open("https://web.roblox.com/home")

    if "minecraft" in text:
        subprocess.Popen('C:\\Program Files (x86)\\Microsoft Studios\\Minecraft Education Edition\\Minecraft.Windows.exe')

    if "chrome" in text:
        subprocess.Popen('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')

    if "pycharm" in text:
        subprocess.Popen('C:\\Program Files\\JetBrains\\PyCharm 2020.3.2\\bin\pycharm64.exe')

    if "spotify" in text:
        subprocess.Popen('C:\\Users\\docto\\AppData\\Roaming\\Spotify\\Spotify.exe')

    if "Notepad" in text:
        subprocess.Popen(["Notepad"])

def play_music(text, onlyfiles):
    print("[Loading Track....]")
    text = text.replace('cortana', '')
    text = text.replace("play", "")

    music_name = text
    query_string = urllib.parse.urlencode({"search_query": music_name})
    formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)

    search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
    clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
    clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])

    inspect = BeautifulSoup(clip.content, "html.parser")
    yt_title = inspect.find_all("meta", property="og:title")

    for concatMusic1 in yt_title:
        pass

    exam = concatMusic1["content"]
    exam = exam.replace(".", "")
    exam = exam.replace(",", "")
    exam = exam.replace("/", "")
    exam = exam.replace(":", "")
    exam = exam.replace("|", "")
    exam = exam.replace("'", "")
    exam = exam + ".mp3"

    exam_path = r"C:\Users\docto\PycharmProjects\Cortana 2.6\Playlist" + "\\" + exam

    check = os.path.exists(exam_path)

    song = concatMusic1


    if check:
        print('Now playing:', concatMusic1['content'], clip2)
        p = vlc.MediaPlayer(exam_path)
        p.play()

        input = sr.Recognizer()
        with sr.Microphone() as source:
            audio = input.listen(source)
            data = ""
            try:
                data = input.recognize_google(audio)
            except:
                pass

        if "stop" in data:
            p.stop()
            tts(inp = "track has ended")

    elif not check:
        tts("[Downloading track...]")

        yt = YouTube(str(clip2))

        video = yt.streams.filter(only_audio=True).first()
        destination = str(r'C:\Users\docto\PycharmProjects\Cortana 2.6\Playlist')

        out_file = video.download(output_path=destination)

        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        print('Now playing:', concatMusic1['content'], clip2)
        p = vlc.MediaPlayer(new_file)
        p.play()

        input = sr.Recognizer()
        with sr.Microphone() as source:
            audio = input.listen(source)
            data = ""
            try:
                data = input.recognize_google(audio)
            except:
                pass

        if "stop" in data:
            p.stop()
            tts(inp="track has ended")


def play_playlist():
    path = 'C:\\Users\\docto\\PycharmProjects\\Cortana 2.6\\Playlist\\'
    num = 0
    file = path + os.listdir(path)[num]
    p = vlc.MediaPlayer(file)
    p.play()
    name = os.listdir(path)[num].replace(".mp3", "")
    print("Now playing:", name)

    while True:
        text = input("Would you like to skip?")
        p.stop()

        if "stop" in text:
            break

        num = num + 1
        file = path + os.listdir(path)[num]
        p = vlc.MediaPlayer(file)
        p.play()
        name = os.listdir(path)[num].replace(".mp3", "")
        print("Now playing:", name)


def play_random():
    music_dir = "C:\\Users\\docto\\PycharmProjects\\Cortana 2.6\\Playlist"
    files = os.listdir(music_dir)
    music = random.choice(files)
    music_name = music.replace(".mp3", "")
    print("Now playing " + music_name)
    p = vlc.MediaPlayer(os.path.join(music_dir, music))
    p.play()

    input = sr.Recognizer()
    with sr.Microphone() as source:
        audio = input.listen(source)
        data = ""
        try:
            data = input.recognize_google(audio)
        except:
            pass

    if "stop" in data:
        p.stop()
        tts(inp="track has ended")







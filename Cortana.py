from chatterbot import ChatBot
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from chatterbot.trainers import ChatterBotCorpusTrainer
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
from gtts import gTTS
import os
import wolframalpha
import time
from playsound import playsound
import playsound
import os.path
import requests
import ctypes
import bs4
from secondary import add_to_playlist, remove, open_app, play_music, play_playlist, play_random, tts
from os import listdir
from os.path import isfile, join

os.system("")
chatbot = ChatBot('Cortana')
trainer = ChatterBotCorpusTrainer(chatbot)
data = ""
authenticator = IAMAuthenticator('IBM API')
text_to_speech = TextToSpeechV1(
        authenticator=authenticator
    )

text_to_speech.set_service_url('URL')


def respond(output):
    print(output)

    with open('text.mp3', 'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(output, voice='en-GB_CharlotteV3Voice',
                                      accept='audio/mp3').get_result().content)

    playsound.playsound('text.mp3')
    os.remove("text.mp3")

def talk():
    input = sr.Recognizer()
    with sr.Microphone() as source:
        audio = input.listen(source)
        data = ""
        try:
            data = input.recognize_google(audio)
            print("You said, " + data)
        except:
            pass

    return data

def error():
    error = 'Request failed'
    speech = gTTS(text=str(error), lang='hi', slow=False)
    print(error)
    speech.save("text.mp3")
    playsound("text.mp3")
    os.remove("text.mp3")

def weather():
    try:
        res = requests.get('https://weather.com/weather/today/l/43.59,-79.64?par=google&temp=c')
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        soup.select('.CurrentConditions--tempValue--3KcTQ')

        for i in soup.select('.CurrentConditions--tempValue--3KcTQ'):
            respond(f'The weather in mississauga is: {i.text}.')
    except:
        error()

def date():
    try:
        from datetime import date
        today = date.today()
        respond(f'Current date is: {today}.')
    except:
        error()

def calc(text):
    try:
        if "calculate" in text:
            text = text.replace('calculate', '')
        if "calculator" in text:
            text = text.replace('calculator', '')

        question = text
        app_id = "WOLFRAM ALPHA API"
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        answer = next(res.results).text
        respond(f"The answer is {answer}")
    except:
        pass

speak = True
if __name__ == '__main__':
    respond("CORTANA ACTIVATED")

    while (1):
        onlyfiles = [f for f in listdir(r"C:\Users\docto\PycharmProjects\Cortana 2.6\Playlist") if isfile(join(r"C:\Users\docto\PycharmProjects\Cortana 2.6\Playlist", f))]
        text = talk().lower()

        if text == 0:
            continue

        elif "exit" in str(text) or "bye" in str(text):
            respond("Bye, I hope that my service has been optimal.")
            quit()

        elif "weather" in text:
            weather()
            speak = False

        elif "date" in text:
            date()
            speak = False

        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for i in numbers:
            if i in text:
                calc(text)
                speak = False
                break

        if "add song" in text or "add track" in text:
            respond("[Finding track....]")
            add_to_playlist(text)
            speak = False

        elif "remove" in text:
            remove(text, onlyfiles)
            speak = False

        elif "playlist" in text and "show" in text:
            speak = False
            count = 0
            for x in onlyfiles:
                x = x.replace(".mp3", "")
                count = count + 1
                print(count, ":", x)

        if "play" in text:
            speak = False
            if "random" in text:
                play_random()
            elif "playlist" in text:
                play_playlist()
            else:
                play_music(text, onlyfiles)


        elif 'research' in text or 'define' in text:
            speak = False
            respond('Searching Wikipedia')
            text = text.replace("wikipedia", "")
            results = wikipedia.summary(text, sentences=3)
            respond("According to Wikipedia")
            respond(results)

        elif 'time' in text:
            speak = False
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            respond(f"the time is {strTime}")

        elif 'search' in text:
            speak = False
            text = text.replace("search", "")
            url = 'https://google.com/search?q=' + text
            webbrowser.open(url)
            time.sleep(5)

        elif 'open' in text:
            speak = False
            text = text.replace('open', "")
            open_app(text)

        elif 'close window' in text:
            speak = False
            respond("locking the device")
            ctypes.windll.user32.LockWorkStation()

        if speak == True:
            try:
                output = chatbot.get_response(text)
            except:
                pass
            respond(str(output))
        












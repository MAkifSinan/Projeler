import speech_recognition as sr
import os
import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
r = sr.Recognizer()
def record(ask = False):
    with sr.Microphone(1) as source:
        if ask:
            print(ask)
            speak(ask)
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio, language='tr')
            print(voice)
        except sr.UnknownValueError:
            print("söylediğiniz anlaşılamadı")
            speak("söylediğiniz anlaşılamadı")
        except sr.RequestError:
            print("sistem yanıt vermiyor")
            speak("sistem yanıt vermiyor")
        return voice
def response(voice):
    if 'nasılsın' in voice:
        print("iyiyim sen nasılsın ?")
        speak("iyiyim sen nasılsın ?")
    if 'saat kaç' in voice:
        print(datetime.datetime.now().strftime('%H:%M:%S'))
        speak(datetime.datetime.now().strftime('%H:%M:%S'))
    if 'arama yap' in voice:
        search = record('ne aramak istiyorsun')
        #if 'çıkış'  in search:

        url = 'https://google.com/search?q='+search
        webbrowser.get().open(url)
        print(search + "search sonuçları ")
        speak(search + "search sonuçları ")
    if 'kendini kapat' in voice:
        speak("tabiki ")
        exit()
    if 'spotify' in voice:
        print("spotify açılıyor")
        speak("spotify açılıyor")
        os.system('Spotify Free')
    time.sleep(1)
def speak(string):
    tts = gTTS(string,lang='tr')
    rand = random.randint(1,10000)
    file = 'audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)
while 1:
    speak("selam!!!! ")
    print("selam!!!! ")
    voice = record()
    voice=voice.lower()
    print(voice)
    response(voice)



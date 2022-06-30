import speech_recognition as sch #record user audio
from time import ctime
import webbrowser #search results
import time
import playsound
import os  #remove audio.mp3 files
import random  #generate multiple audio.mp3 files
from gtts import gTTS #text to speech

r = sch.Recognizer()  # recognise user audio.

def arya_speak(audio_string):  # assistant speaks the converted text strings
    text_to_speech = TTS(text = audio_string, lang='en')
    r = random.randint(1,10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    text_to_speech.save(audio_file)
    playsound.playsound(audio_file) # mp3 files generated are played
    print(audio_string) # assistant speaks and the spoken lenes are printed in console/terminal
    os.remove(audio_file)


def take_audio_from_user(ask = False):
    if ask:
        arya_speak(ask)
    with sch.Microphone() as source:
    audio = r.listen(source)   # user input gets stored in audio
    voice_data = ''
    try:
        voice_data = r.recognize_google(audio)   # assistant recognise our audio and analyse it by this function call
    except sch.UnknownValueError:
        arya_speak('sorry could you repeat')  # irregular input
    except sch.RequestError:
        arya_speak('sorry, i am not available at this moment')
    return voice_data


def respond_to_user(voice_data):
    # replies it's name
    if 'what is your name' in voice_data:
        arya_speak('My name is Arya')

    # replies current time
    if 'what time is it' in voice_data:
        arya_speak(ctime())

    # replies search details
    if 'search' in voice_data:
        search = take_audio_from_user('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        arya_speak ('Here is what I found for ' + search)

    # locate the places
    if 'locate' in voice_data:
        location = take_audio_from_user('Which place do i need to locate?')
        url = 'https://google.nl/maps/place/' + location + '/&amp'
        webbrowser.get().open(url)
        arya_speak ('I have located ' + search)

    # exit of assistant
    if 'exit' in voice_data:
        exit()

# takes input and reply as long as exit has been told
time.sleep(1):
arya_speak('how can i help you?')
while 1:
    voice_data = take_audio_from_user()
    respond_to_user(voice_data)





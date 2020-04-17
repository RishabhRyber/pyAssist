import os
import speech_recognition as sr
from time import sleep
from gtts import gTTS
import webbrowser
import winsound
r = sr.Recognizer()

def shutdown(time=0):
    speak('Sir, Are You sure to shut down the system. Make sure that all opened files are saved')
    if "yes" in listenSource():
        speak("OK Sir, The system will shut down in a while.")
        speak('OK Sir, shutting down your computer')
        os.system("shutdown -s /t " +str(time))
    else:
        speak("Fluctuating mind,huh!")

def openBrowser(website="nahinAyaHai"):
    if website=="nahinAyaHai":
        webbrowser.open_new_tab("http://www.google.com")


def openYoutube(songName="nahinAyaHai"):
    if songName=="nahinAyaHai":
        webbrowser.open_new_tab("http://www.youtube.com")

def closeAssistance():
    speak('Sir, Are You sure to close me')
    if "yes" in listenSource():
        speak("OK Sir, I will go offline in a while.")
    sleep(3)
    quit()

def speak(textToSpeech):
    tts = gTTS(textToSpeech, lang='en')  # gTTS requires internet connection...
    tts.save("textToSpeech.wav")
    print(textToSpeech)
    # winsound.PlaySound("textToSpeech",winsound.SND_FILENAME)


def listenSource():
    print("Say Something!")
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        voiceInput = r.recognize_google(audio)
        return  voiceInput
    except sr.UnknownValueError:
        return "nahinPtaChala"  #to trace error in listening. google API will never detect this so it's error only

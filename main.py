import os
import speech_recognition as sr
from time import sleep
from gtts import gTTS

import jobs
import re

# r = sr.Recognizer()


def executeCommands(command):
    print(command)

    if "nahinPtaChala" in command:
        jobs.speak("Soory Failed To Understand You, Please Try again.")

    if "open" in command:
        if "YouTube" in command:
            jobs.openYoutube()
        if "browser" or "chrome" in command:
            jobs.openBrowser()
    if "shutdown" in command:
        time=0
        # try:
        time=int(re.search(r'\d+', command).group())
        if "minute" in command:
            time=time*60
        elif "hour" in command:
            time=time*60*60
        jobs.shutdown(time)
        # except re.AttributeError:
        #     jobs.shutdown(0)

    if "close" in command:
        jobs.closeAssistance()




jobs.speak("hello dude,I am ready to follow")
while True:
    command=jobs.listenSource()
    executeCommands(command)
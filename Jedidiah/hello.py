# import gtts
# from playsound import playsound
# tts = gtts.gTTS('Hello')
# tts.save('hello.mp3')
# # playsound('hello.mp3')
# 
# import pyttsx
# engine = pyttsx.init()
# engine.say('hello')
# engine.runAndWait()

# from gtts import gTTS
# import os
# tts = gTTS(text='Good morning', lang='en')
# tts.save("good.mp3")
# os.system("mpg321 good.mp3")

from gtts import gTTS
import os

s = 'escape with plane'
file = 'file.mp3'
tts = gTTS(s, 'en')
tts.save(file)
os.system('mp123 ' + file)
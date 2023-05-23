import espeak
espeak.init()
speaker = espeak.Espeak()
speaker.say("Hello")
speaker.rate = 300
speaker.say("Hello again")
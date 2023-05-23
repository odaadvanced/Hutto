from gtts import gTTS

myText = '''And now to home I shall fly.
To this very red planet- goodbye.
I have finished my errand.
Here’s the message I shall send
To travel back through the stars:
There are signs of life on Mars.'''

language = 'en'

output = gTTS(text = myText, lang = language, slow = False)

output.save("short_poem.mp3")

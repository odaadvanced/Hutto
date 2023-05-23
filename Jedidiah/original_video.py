from gtts import gTTS

myText = '''We have just landed on Mars. This place is strange and bizarre.
We are searching for signs of life. Can one stand here alive?
To those who think Mars red. To those who think its dead.
To those who think it melts by day, And freezes when night holds sway.
To those who think its rocky. To those who think its chalky.
To thse who think the skies above, Are as pink as you can think of.
I, educated Martian rover, Shall defeat those myths that hover.
You are terribly mistaken. You've been fooled all your life and shaken.
Mars is honestly quite queer. I'll educate you, never fear.
The temperature here is mild. The number of obstacles- wild.
This place is surprisingly bright. Its rather flooded with light.
The ground beneath is rather gray, The horizons blue one way.
The other way its sickly green. What this means is yet unseen.
Its something I shall ponder. While this vast terrain I wander.
On this journey my sole object. Is to help three kids on their project.
Tell those earthlings down below. They can speed here- no one will know.
Not that I can really speed, I am just a rover I concede.
I will capture all I can, I will take a shot at that man,
And send it all down to earth- To that blazing Texas herth.
This place is dreary and bleak. I hear my tires squeak.
But other than that. Theres no sound on this flat.
I quietly creep like a cat. But wait! What noise was that?
Perhaps some squeaking of shoes? Oh, danger overhead brews!
Does Mars hold aliens? Or worse yet- dreadful humans?
I shall haste to finish my job. And then fly from this creepy mob.
For now, I better be silent. Humans are eavesdropping agents.'''

language = 'en'

output = gTTS(text = myText, lang = language, slow = False)

output.save("output.mp3")

Nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango",
"extrovert", "gorilla"]
Verbs = ["kicks", "jingles", "bounces", "slurps", "meows",
"explodes", "curdles"]
Adjectives = ["furry", "balding", "incredulous", "fragrant",
"exuberant", "glistening"]
Prepositions = ["against", "after", "into", "beneath", "upon",
"for", "in", "like", "over", "within"]
Adverbs = ["curiously", "extravagantly", "tantalizingly",
"furiously", "sensuously"]
article1 = "A"
article2 = "An"

import random

def pick_words():
    global Nouns
    global Verbs
    global Adjectives
    global Prepositions
    global Adverbs
    global article1
    global article2
    noun1 = random.choice(Nouns)
    noun2 = random.choice(Nouns)
    noun3 = random.choice(Nouns)
    verb1 = random.choice(Verbs)
    verb2 = random.choice(Verbs)
    verb3 = random.choice(Verbs)
    adj1 = random.choice(Adjectives)
    adj2 = random.choice(Adjectives)
    adj3 = random.choice(Adjectives)
    prep1 = random.choice(Prepositions)
    prep2 = random.choice(Prepositions)
    adverb1 = random.choice(Adverbs)
    if adj1[0] in "aeiou":
        adj1 = "An " + adj1
    else:
        adj1 = "A " + adj1
    print(f"{adj1} {noun1}")
    print(f"{adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}")
    print(f"{adverb1}, the {noun1} {verb2}")
    print(f"the {noun2} {verb3} {prep2} a {adj3} {noun3}")
pick_words()
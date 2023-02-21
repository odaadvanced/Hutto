import random

nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango",
         "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows",
         "explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant",
              "exuberant", "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon",
                "for", "in", "like", "over", "within"]
adverbs = ["curiously", "extravagantly", "tantalizingly",
           "furiously", "sensuously"]

def picker(item):
    random_word = random.choice(item)
    return random_word

def poem_generator():
    first_adj = picker(adjectives)
    if first_adj[0] in ("aeiou"):
        article = "an"
    else:
        article = "a"
    poem_generator_words = [article, first_adj]
    return poem_generator_words

poem_generator_2 = poem_generator()
title_2 = f"{poem_generator_2[0].title()} {poem_generator_2[1]} {picker(nouns)}"
print(f'''{title_2}

{title_2} {picker(verbs)} {picker(prepositions)} the {picker(adjectives)} {picker(nouns)}
{picker(adverbs)}, the {picker(nouns)} {picker(verbs)}
the {picker(nouns)} {picker(verbs)} {picker(prepositions)} {poem_generator()[0]} {poem_generator()[1]} {picker(nouns)}''')

nouns = ["fossil", "horse", "aadvark", "jungle", "chef", "mango", "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

import random

adj1 = random.choice(adjectives)
if adj1[0] in ["a", "e", "i", "o", "u"]:
    article = "an"
else:
    article = "a"

noun1 = random.choice(nouns)
verb1 = random.choice(verbs)
prep1 = random.choice(prepositions)
adj2 = random.choice(adjectives)
noun2 = random.choice(nouns)
adverb1 = random.choice(adverbs)
verb2 = random.choice(verbs)
verb3 = random.choice(verbs)
prep2 = random.choice(prepositions)
adj3 = random.choice(adjectives)
noun3 = random.choice(nouns)

print(f"""{article.capitalize()} {adj1} {noun1}

{article.capitalize()} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}
{adverb1}, the {noun1} {verb2}
the {noun2} {verb3} {prep2} a {adj3} {noun3}""")
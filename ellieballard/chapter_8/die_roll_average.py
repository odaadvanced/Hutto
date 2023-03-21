import random

def die_roll_average():
    die_total = 0
    for i in range (10000):
        die = random.randint(1,6)
        die_total = die_total + die
    return die_total/10000

print (die_roll_average())
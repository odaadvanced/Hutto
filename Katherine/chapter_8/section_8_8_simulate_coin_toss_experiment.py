import random

total_flips = 0
trial_flips = 0

def coin_flip():
    global heads_tally
    global tails_tally
    global total_flips
    global trial_flips
    while (heads_tally < 1 or tails_tally < 1):
        if random.randint(0,1) == 0:
            heads_tally = heads_tally + 1
        else:
            tails_tally = tails_tally + 1
    total_flips = heads_tally + tails_tally
    trial_flips = trial_flips + total_flips
    return trial_flips

for trial in range(10_000):
    heads_tally = 0
    tails_tally = 0
    coin_flip()

print((trial_flips)/10_000)
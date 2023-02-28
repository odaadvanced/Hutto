import random
def coin_flip():
    if random.randint(0,1) == 0:
        return "heads"
    else:
        return "tails"


def avg_flips():
    total_flips = 0
    for trial in range (10000):
        heads_tally = 0
        tails_tally = 0
        num_of_flips = 0
        while (heads_tally == 0) or (tails_tally == 0):
            if coin_flip() == "heads":
                heads_tally = heads_tally + 1
                num_of_flips = num_of_flips + 1
            else:
                tails_tally = tails_tally + 1
                num_of_flips = num_of_flips + 1
        total_flips = total_flips + num_of_flips
    return total_flips / 10000

print (avg_flips())
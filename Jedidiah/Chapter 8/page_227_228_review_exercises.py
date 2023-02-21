import random
number_won = 0

def wins_region(percent):
    if random.random() <= percent / 100:
        return 1
    else:
        return 0

for election in range(10000):
    if wins_region(87) + wins_region(65) + wins_region(17) >= 2:
        number_won = number_won + 1

print(f"Candidate A wins {number_won} times.")
    
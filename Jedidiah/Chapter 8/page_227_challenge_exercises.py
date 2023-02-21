import random

def fair_coin():
    value = random.randint(0,1)
    if value == 1:
        return True
    else:
        return False


total_flip = 0
for i in range(10000):
    boolean = fair_coin()
    flip = 1
    while fair_coin() == boolean:
        flip = flip + 1
    flip += 1
    total_flip = total_flip + flip

print(f" The average number of flips per trial is {(total_flip / 10000)}")
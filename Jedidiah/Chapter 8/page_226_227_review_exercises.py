import random
sum = 0

def roll():
    number = random.randint(1,6)
    return number

for dice in range(10000):
    sum = sum + roll()

average = sum / 10000
print(average)
import random

total = 0
for trial in range(10000):
    x = random.randint(1,6)
    total = total + x

average = (total) / 10000
print(average)
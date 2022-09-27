#03_04_double_dice_while
import random
throw_1 = random.randint(1, 6)
throw_2 = random.randint(1, 6)
count = 1
while not (throw_1 == 6 and throw_2 == 6):
	total = throw_1 + throw_2
	count = count + 1
	print(total)
	throw_1 = random.randint(1, 6)
	throw_2 = random.randint(1, 6)
print ('Finished!')
print (count)
print('Double Six thrown!')
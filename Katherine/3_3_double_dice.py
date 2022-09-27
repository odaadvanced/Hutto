#3_3_double_dice.py
#import random
#for x in range (1, 11):
 #   throw_1 = random.randint (1, 6)
  #  throw_2 = random.randint (1, 6)
   # total = throw_1 + throw_2
    #print (total)
#    if total == 7:
 #       print ('Seven Thrown')
 #   if total == 11:
  #      print ('Eleven Thrown')
   # if throw_1 == throw_2:
    #    print ('Double Thrown')
  #  if total > 10:
   #     print ('Good Throw!')
   # if total < 4:
    #    print ('Unlucky!')
import random
throw_1 = random.randint (1,6)
throw_2 = random.randint (1,6)
while not (throw_1 == 6 and throw_2 == 6):
    total = throw_1 + throw_2
    throw_1 = random.randint (1,6)
    throw_2 = random.randint (1,6)
    print (total)
print ('Double Six thrown!')
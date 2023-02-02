response1 = float(input("Enter a number: "))
response2 = float(input("Enter another number: "))
difference = response1 - response2
print ("The difference between " + str(response1) + " and " + str(response2) + " is an integer? " + str(difference.is_integer()))
cardinal_number = ("first", "second", "third")
print("This is the string at index 1 in cardinal_numbers: " + cardinal_number[1])
position1, position2, position3 = cardinal_number
print("These are the values in cardinal_numbers unpacked: ")
for position in cardinal_number:
    print(position)
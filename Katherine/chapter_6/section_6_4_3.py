def doubles(number):
    number = number * 2
    return number

number = 2

for k in range(1, 4):
    print(doubles(number))
    number = doubles(number)
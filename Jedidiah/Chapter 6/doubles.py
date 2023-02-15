def doubles(x):
    number = x * 2
    return number

num = 2
for i in range(3):
    print(doubles(num))
    num = doubles(num)
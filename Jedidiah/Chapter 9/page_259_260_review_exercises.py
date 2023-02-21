data = ((1,2), (3,4))
number = 1
for num in data:
    print(f"Row {number} sum: {sum(num)}")
    number = number + 1

numbers = [4, 3, 2, 1]
numbers_2 = numbers[:]
numbers.sort()
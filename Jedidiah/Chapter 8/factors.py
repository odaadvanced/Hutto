num = int(input("Enter a positive integer: "))
for number in range(1, num+1):
    if num % number == 0:
        print(f"{number} is a factor of {num}")
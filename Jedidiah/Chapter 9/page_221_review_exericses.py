try:
    prompt = int(input("Enter an integer: "))
except ValueError:
    prompt = input("That was not an integer. Please try again: ")
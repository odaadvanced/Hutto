try:
    prompt_1 = input("Enter a string: ")
    prompt_2 = int(input("Enter an integer: "))
    print(prompt_1[prompt_2])

except ValueError:
    print("That value is not an integer value.")

except IndexError:
    print("That integer value is out of bounds.")
    
while True:
    try:
        prompt = int(input("Enter an integer: "))
        print(f"You entered: {prompt}")
        break

    except ValueError:
        prompt_2 = input("That was not an integer. Please try again: ")
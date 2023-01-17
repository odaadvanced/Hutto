first_prompt = "Enter a number."
first_user_input = input(first_prompt)
second_prompt = "Enter a second number."
second_user_input = input(second_prompt)
product = int(first_user_input)*int(second_user_input)
print("The product of " + str(first_user_input) + " and " + str(second_user_input) + " is " + str(float(product)))
prompt_1 = "Enter a base: "
user_input_1 = input(prompt_1)
prompt_2 = "Enter an exponent: "
user_input_2 = input(prompt_2)
answer = float(user_input_1) ** float(user_input_2)
print(str(user_input_1) + " to the power of " + str(user_input_2) + " = " + str(answer))
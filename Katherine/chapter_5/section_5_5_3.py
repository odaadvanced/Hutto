prompt_1 = "Enter a number: "
user_input_1 = input(prompt_1)
prompt_2 = "Enter another number: "
user_input_2 = input(prompt_2)
if (float(user_input_1) - float(user_input_2)).is_integer():
    print("The difference between " + str(user_input_1) + " and " + str(user_input_2) + " is an integer? True!")
else:
    print("The difference between " + str(user_input_1) + " and " + str(user_input_2) + " is an integer? False!")
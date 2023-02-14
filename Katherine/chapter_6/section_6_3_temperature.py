def convert_far_to_cel(F):
    """Converts degrees Fahrenheit to degrees Celsius."""
    C = (F - 32) * 5/9
    return float(C)

def convert_cel_to_far(C):
    """Converts degrees Celsius to degrees Fahrenheit."""
    F = C * 9/5 + 32
    return float(F)

prompt_1 = "Enter a temperature in degrees F: "
user_input_1 = float(input(prompt_1))
print(f"{user_input_1} degrees F = {convert_far_to_cel(user_input_1):.2f} degrees C")

prompt_2 = "Enter a temperature in degrees C: "
user_input_2 = float(input(prompt_2))
print(f"{user_input_2} degrees C = {convert_cel_to_far(user_input_2):.2f} degrees F")
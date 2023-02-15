def convert_cel_to_far(C):
    F = C * 9/5 + 32
    return F

def convert_far_to_cel(F):
    C = (F - 32) * 5/9
    return C

prompt1 = input("Enter a temperature in degrees Farenheit: ")
print(f"{float(prompt1)} degrees F = {convert_far_to_cel(float(prompt1)):.2f} degrees C")
prompt2 = input("Enter a temperature in degrees Celsius: ")
print(f"{float(prompt2)} degrees C = {convert_cel_to_far(float(prompt2)):.2f} degrees F")
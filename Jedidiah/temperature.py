def convert_cel_to_far(C):
    F = C * 9/5 + 32
    return F

def convert_far_to_cel(F):
    C = (F - 32) * 9/5
    return C

prompt1 = input("Enter a temperature in degrees Farenheit: ")
print(f"{float(prompt1)} degrees F = 
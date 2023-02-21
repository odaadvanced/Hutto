def convert_cel_to_far(C):
    F = C * 9/5 + 32
    return F
    
C = float(input("Enter a temperature in degrees C: "))
temp_in_far = convert_cel_to_far(C)
print(format(temp_in_far, ".2f"))

def convert_far_to_cel(F):
    C = (F - 32) * 5/9
    return C

F = float(input("Enter a temperature in degrees F: "))
temp_in_cel = convert_far_to_cel(F)
print(format(temp_in_cel, ".2f"))
prompt1 = input("Enter a number: ")
prompt2 = input("Enter another number: ")
float1 = float(prompt1)
float2 = float(prompt2)
difference = float1 - float2
boolean = difference.is_integer()
print(f"The difference between {float1} and {float2} is an integer? {boolean}!")
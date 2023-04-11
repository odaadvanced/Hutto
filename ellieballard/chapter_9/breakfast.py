string = "eggs, fruit, orange juice"
breakfast = string.split(", ")
print(breakfast)
print(len(breakfast))
lengths = [len(element) for element in breakfast]
print(lengths)
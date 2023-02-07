total = 0

def add_to_total(n):
    global total #use the global total
    total = total + n

add_to_total(5)
print(total)
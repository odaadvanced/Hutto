def my_func (a, b):
    c = a ** b
    return c

for i in range(1, 4):
    j = i * 2
    d = my_func(i, j)
    print(f"i is {i} and j is {j} and {d}")
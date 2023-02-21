list_dict = [False, False, True, False]
for j in range(1, 5):
    for k in range(4):
        if (k+1) % j == 0:
            if list_dict[k] == False:
                list_dict[k] = True
            else:
                list_dict[k] = False
        else:
            print((k+1) % j)
print(list_dict)
list_dict = []
list_set = []
for i in range(100):
    list_dict.append(False)
    
for j in range(1, 101):
    for k in range(100):
        if (k+1) % j == 0:
            if list_dict[k] == False:
                list_dict[k] = True
            else:
                list_dict[k] = False

for l in range(0,100):
    if list_dict[l] == True:
        list_set.append(l+1)
        
print(list_set)
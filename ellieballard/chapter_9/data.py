data = ((1,2), (3,4))
index = 0
for row in data:
    print("Row " + str(index + 1) + " sum: " + str((data[index][0] + data[index][1])))
    index = index + 1
# Exercise 1

import pathlib
path = pathlib.Path.home() / 'starships.txt'
lines_of_text = [
    "Discovery\n",
    "Enterprise\n",
    "Defiant\n",
    "Voyager\n"
    ]
with path.open(mode='w', encoding='utf-8') as file:
    file.writelines(lines_of_text)

# Exercise 2
with path.open(mode='r', encoding='utf-8') as file:
    for line in file.readlines():
        print(line, end='')

# Exercise 3
print('\n')
with path.open(mode='r', encoding='utf-8') as file:
    for line in file.readlines():
        if line[0] == 'D':
            print(line, end='')
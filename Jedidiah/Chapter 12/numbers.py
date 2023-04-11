# Exercises for number 1.

from pathlib import Path
import csv

numbers = [
[1, 2, 3, 4, 5],
[6, 7, 8, 9, 10],
[11, 12, 13, 14, 15],
]

file_path = Path.home() / 'numbers.csv'
with file_path.open(mode='a', encoding='utf-8') as file:
    writer = csv.writer(file)
    for number in numbers:
        writer.writerow(number)
    
# Exercises for number 2.    

number_list = []
with file_path.open(mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        int_row = [int(value) for value in row]
        number_list.append(int_row)

print(number_list)

# Exercises for number 3.

favorite_colors = [
    {"name": "Joe", "favorite_color": "blue"},
    {"name": "Anne", "favorite_color": "green"},
    {"name": "Bailey", "favorite_color": "red"},
    ]

file_path = Path.home() / "favorite_colors.csv"
file = file_path.open(mode="w", encoding="utf-8")
writer = csv.DictWriter(file, fieldnames =["name", "favorite_color"])
writer.writeheader()
writer.writerows(favorite_colors)
file.close()

# Exercises for number 4

favorite_colors = []
with file_path.open(mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        favorite_colors.append(row)
print(favorite_colors)

from pathlib import Path
import csv

favorite_colors = []
file_path = Path.home() / "favorite_colors.csv"
file = file_path.open(mode='r', encoding='utf-8')
reader = csv.DictReader(file)
reader.fieldnames
for row in reader:
    favorite_colors.append(row)
print(favorite_colors)
file.close()
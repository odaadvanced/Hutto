from pathlib import Path
import csv

file_path = Path.home() / "employees.csv"
file = file_path.open(mode="r", encoding="utf-8")
reader = csv.DictReader(file)
#reader.fieldnames
print(reader)

for row in reader:
    print(row)

file.close()
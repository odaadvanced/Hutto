import pathlib

home = pathlib.Path.home()
file_path = home / "my_folder/my_file.txt"
print(file_path.name)
print(file_path.parent.name)
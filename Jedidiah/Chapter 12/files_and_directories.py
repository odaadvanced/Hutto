# Review Exercises pp. 357-358 #1

import pathlib

my_folder = pathlib.Path("/home/pi/my_folder")
my_folder.mkdir()

# Review Exercises # 2
file1 = my_folder / "file1.txt"
file2 = my_folder / "file2.txt"
image1 = my_folder / "image1.png"

file1.touch()
file2.touch()
image1.touch()

# Review Exercises # 3

images = pathlib.Path.home() / "images"
images.mkdir()
source = image1
destination = images / "image1.png"
source.replace(destination)

# Review Exercises # 4
file1.unlink()

# Review Exercises # 5

import shutil
shutil.rmtree(my_folder)
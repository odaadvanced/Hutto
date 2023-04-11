import pathlib

images = pathlib.Path.home() / "Chapter_12_Practice_Files_Folder" / "images"
images.mkdir()

Chapter_12_Practice_Files_Folder = pathlib.Path.home() / "Chapter_12_Practice_Files_Folder"
for image in Chapter_12_Practice_Files_Folder.rglob("*.png"):
    source = image
    destination = images / image.name
    source.replace(destination)

for image in Chapter_12_Practice_Files_Folder.rglob("*.gif"):
    source = image
    destination = images / image.name
    source.replace(destination)

for image in Chapter_12_Practice_Files_Folder.rglob("*.jpg"):
    source = image
    destination = images / image.name
    source.replace(destination)
    
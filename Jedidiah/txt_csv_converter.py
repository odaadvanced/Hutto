# copies information from .txt files to .csv files
from pathlib import Path
import csv

def converter(file_name):
    new_path_name = file_name.stem + '.csv'    
    new_file_path = Path.home()/f'{new_path_name}'
    new_file_path.touch()
    with open(file_name, mode = 'r', encoding = 'utf-8') as file:
        text = file.read()
    return new_file_path

def copy_information(filename):
    old_file_name = converter(file_name).stem + '.txt'
    old_file_path = Path.home()/f'{old_file_name}'
    
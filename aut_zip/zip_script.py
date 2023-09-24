"""
Zip with python
"""
from zipfile import ZipFile
import os

path = ":\Your\Full\Path"
with ZipFile('file.zip', 'w') as zip:
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        zip.write(full_path, path)
        

    with ZipFile('file.zip', 'r') as zip:
        for file in zip.namelist():
            print(file)

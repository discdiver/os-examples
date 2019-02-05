# path.py
import os

cwd = os.getcwd()

for dir_path, dir_names, file_names in os.walk(cwd):
    for f in file_names:
        print(f)

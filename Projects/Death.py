import glob
import os

path = r"C:\Users\jritter\Desktop\death\*"

for file_path in glob.glob(path):
    answer = input(f"Do you want to delete {file_path}? (y/n): ").strip().lower()

    if answer == "y":
        os.remove(file_path)
        print(f"Deleting {file_path}")
    elif answer == "n":
        print(f"Skipping {file_path}")


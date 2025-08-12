import glob
import os

# Get the list of all files and directories
path = r"C:\users\*"
dir_list = glob.glob(path)

print(f"Files and directories in '{path}':")
print(dir_list)
print(len(dir_list))

for item in dir_list:
    if os.path.isdir(item):
        print(item)

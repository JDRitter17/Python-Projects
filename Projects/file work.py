import glob
import os

# Search all user directories
path = r"C:\users\*"
apple_found = False
dir_list = glob.glob(path)

print(f"Files and directories in {path}: {dir_list}")
print(dir_list[0])
print(len(dir_list))

# Check if any directory contains "rappleto"
for item in dir_list:
    if "rappleto" in item:
        apple_found = True

if apple_found:
    print("Yes")
else:
    print("No")

# Check if the first item is a directory or file
if os.path.isdir(dir_list[0]):
    print(f"{dir_list[0]} is a directory")
elif os.path.isfile(dir_list[0]):
    print(f"{dir_list[0]} is a file")

# Find total size and most recent file in a given directory
latest_mod_time = 0
recent_file = ""
total_size = 0

path2 = r"C:\Users\jritter\Desktop\*"
for item in glob.glob(path2):
    print(item)
    status = os.stat(item)
    total_size += status.st_size
    mod_time = status.st_mtime

    if mod_time > latest_mod_time:
        latest_mod_time = mod_time
        recent_file = item

print(f"The size of all files in the directory is {total_size} bytes")
print(f"{recent_file} is the most recent file accessed")

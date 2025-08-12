import os
import shutil

src = r"C:\Users\jritter\Desktop\Src"
dest = r"C:\Users\jritter\Desktop\Dest"

def compareFiles(src_file, dest_file):
    # Copy src_file to dest_file if dest_file doesn't exist or src_file is newer
    if not os.path.isfile(dest_file) or os.path.getmtime(src_file) > os.path.getmtime(dest_file):
        print(f"Copy {src_file} -> {dest_file}")
        shutil.copy2(src_file, dest_file)
    else:
        print(f"NoCopy {src_file} -> {dest_file}")

for root, dirs, files in os.walk(src, topdown=True):
    # Create any directories in dest that exist in src
    for name in dirs:
        src_dir = os.path.join(root, name)
        dest_dir = src_dir.replace(src, dest)
        if not os.path.isdir(dest_dir):
            os.makedirs(dest_dir)
            print(f"Making directory: {dest_dir}")

    # Copy files if needed
    for name in files:
        src_file = os.path.join(root, name)
        dest_file = src_file.replace(src, dest)
        compareFiles(src_file, dest_file)

import os
import datetime

path = r"C:\Users\jritter\Desktop\cars.txt"

try:
    file_stats = os.stat(path)
    print(file_stats.st_size)
    mtime = file_stats.st_mtime
    print(datetime.datetime.fromtimestamp(mtime))

except FileNotFoundError:
    print("File not found!")
except Exception as e:
    print(f"An error occurred: {e}")

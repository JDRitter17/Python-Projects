import os

biggest_num = 0
biggest_path = ""

for root, dirs, files in os.walk(r"C:\Users\jritter\Desktop"):
    for file in files:
        file_path = os.path.join(root, file)
        count = file_path.count("\\")  # Count backslashes in the path

        if count > biggest_num:
            biggest_num = count
            biggest_path = file_path

print(f"The biggest filepath is: {biggest_path} with {biggest_num} backslashes")

import os

file_list = []

for root, dirs, files in os.walk(r"C:\Users\jritter\Desktop"):
    for file in files:
        file_path = os.path.join(root, file)
        size = os.stat(file_path).st_size
        file_list.append([size, file_path])

# Sort list by size in descending order
file_list.sort(reverse=True)

print("Top 5 Biggest Files:")
for i in range(min(5, len(file_list))):
    print(f"{file_list[i][1]}, {file_list[i][0]} bytes")

home_dirs = {}

with open(r'C:\Users\jritter\Desktop\passwd.txt', 'r') as f:
    for line in f:
        items = line.split(':')
        name = items[0]
        home_dir = items[5]
        home_dirs[name] = home_dir

for user, directory in home_dirs.items():
    print(f"{user} has directory {directory}")

if 'jritzer' in home_dirs:
    print("yes")

if '/home/makersho' in home_dirs.values():
    print("yes")

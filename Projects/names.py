names = {}

with open(r'C:\Users\jritter\Desktop\names.txt', 'r') as f:
    for line in f:
        name = line.strip()
        if name in names:
            names[name] += 1
        else:
            names[name] = 1

print(names)

highest = 0
highest_name = ""

for name, count in names.items():
    if count > highest:
        highest = count
        highest_name = name

print(f"{highest_name} appears the most with {highest}")





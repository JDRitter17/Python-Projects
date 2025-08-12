import glob

numbers = [[1, 100], [2, -200], [-3, 300], [-4, 400], [5, -500], [-6, 600]]

total = 0
for num in numbers:
    if num[1] > 0:
        total += num[1]
print(total)

for num in range(1, 7):
    for num2 in range(1, 4):
        print(f"{num} {num2}")

path = r"C:\Users\jritter\Desktop\*"
print(len(glob.glob(path)))

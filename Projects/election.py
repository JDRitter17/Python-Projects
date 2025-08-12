with open(r"C:\Users\jritter\Desktop\elections-data.txt", "r") as f:
    junk = f.readline()  # skip header line
    data = []

    for line in f:
        district, pvi = line.strip().split(",")
        party = pvi[0]
        number_str = pvi[2:].strip()

        if party == "E":
            number = 0
        elif party == "R":
            number = -int(number_str)
        else:
            number = int(number_str)

        data.append([number, district])

# Sort by number (first item in the sublist)
data.sort(key=lambda x: x[0])

print(data)
middle = data[len(data) // 2]
print(f"Median entry: {middle}")

total = sum(d[0] for d in data)
count = len(data)

print(f"The average is {total / count}")

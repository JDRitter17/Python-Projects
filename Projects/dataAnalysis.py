with open(r"C:\Users\jritter\Desktop\football.txt", "r") as f:
    data = []
    for line in f:
        team, golfscore = line.strip().split(",")
        number = float(golfscore)
        data.append([team, number])

# Calculate middle index (integer division)
middle_index = len(data) // 2

# Sort data by team name (default sort on first element)
data.sort(key=lambda x: x[0])

print(f"The middle team is {data[middle_index][0]}")

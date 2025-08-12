with open(r"C:\Users\jritter\Desktop\us-state-capitals.csv", "r") as f:
    most_south = float('inf')  # large number for comparison
    total_lat = 0.0
    count = 0
    south_cap = ""

    for line in f:
        data = line.strip().split(",")
        lat = float(data[2])
        cap = data[1]

        total_lat += lat
        count += 1

        if lat < most_south:
            most_south = lat
            south_cap = cap

avg_lat = total_lat / count
print(f"The average latitude is {avg_lat}")
print(f"The southernmost capital is {south_cap} at latitude {most_south}")

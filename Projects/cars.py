# Open the file safely using 'with' to ensure it closes automatically
with open(r"C:\Users\jritter\Desktop\cars.txt", "r") as f:
    highest = 0
    highest_car = None

    for line in f:
        data = line.strip().split(",")
        # Calculate acceleration ratio (assuming data[3] and data[4] are convertible to float)
        try:
            compare = float(data[3]) / float(data[4])
        except (ValueError, ZeroDivisionError):
            # Skip lines with invalid data or division by zero
            continue

        if compare > highest:
            highest = compare
            highest_car = data[8].strip()

print(f"The car with the highest acceleration is {highest_car} at {highest}")

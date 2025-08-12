f = open("C:\\Users\\jritter\\Desktop\\cars.csv", "r")
junk=f.readline()
lineCount = 0
biggestWeight = 0
biggestModel = ""
cylindersCount = 0
for line in f:
    lineCount += 1
    data = line.split(",")
    model = data[8].rstrip()
    weight = int(data[4])
    print(f"{model} weighs {data[4]} lbs")
    print(data)
    if weight > biggestWeight:
        biggestWeight = weight
        biggestModel = model
    cylinders = int(data[1])
    if cylinders == 8:
        cylindersCount += 1


print(f"The {biggestModel} weighs the most at {biggestWeight} lbs")
print(f"There are {lineCount} cars")
print(f"There are {cylindersCount}, 8 cylinders cars")
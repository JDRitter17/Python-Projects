holiday_rate = {}

with open(r'C:\Users\jritter\Desktop\hoidays.txt', 'r') as f:
    for line in f:
        items = line.strip().split(",")
        holiday = items[0].strip()
        rate = int(items[1].strip())
        holiday_rate[holiday] = rate

while True:
    your_holiday = input("Give a holiday: ")

    if your_holiday in holiday_rate:
        print(holiday_rate[your_holiday])

    your_rating = int(input("Give a rating: "))

    for holiday, rating in holiday_rate.items():
        if rating == your_rating:
            print(holiday)

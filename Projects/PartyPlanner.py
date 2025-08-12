ages = []
drinkAges = []
kidAges = []

def getAges():
    x = 1
    while True:
        try:
            age = int(input(f"Please enter the age of guest #{x} (or -1 to finish): "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if age == -1:
            break
        if age < 0:
            print("Please enter a positive age or -1 to finish.")
            continue

        ages.append(age)

        if age >= 21:
            drinkAges.append(age)
        elif age < 21:
            kidAges.append(age)

        x += 1

    print(f"All ages: {ages}")
    print(f"Kid ages (<21): {kidAges}")
    print(f"Over 21 ages: {drinkAges}")

def Beers(age_list):
    beer = 2 * len(age_list)
    print(f"You need {beer} beers")

def Brats(age_list):
    brat = 0
    for age in age_list:
        if age >= 21:
            brat += 2
        else:
            brat += 1
    print(f"You need {brat} brats")

def Soda(age_list):
    soda = 2 * len(age_list)
    print(f"You need {soda} sodas")

# Run the functions
getAges()
Beers(drinkAges)
Brats(ages)
Soda(kidAges)

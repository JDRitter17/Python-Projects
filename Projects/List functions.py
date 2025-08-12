l = [10, 11, 12, 13, 14]

def printThird(lst):
    third_item = lst[2]
    print(f"The third item in the list is {third_item}")

printThird(l)

def getThird(lst):
    return lst[2]

q = getThird(l)
print(f"The third item in the list is {q}")

def pairItem(lst):
    average = (lst[-1] + lst[-2]) / 2
    return average

average = pairItem(l)
print(f"The average of the last two items is {average}")

def goesUp(lst):
    # Returns True if first item is greater than last, False otherwise
    return lst[0] > lst[-1]

upSlope = goesUp(l)
if upSlope:
    print("You got this right")
else:
    print("Poop!")

def getEvens(lst):
    evens = [i for i in lst if i % 2 == 0]
    return evens

q = getEvens(l)
print(f"The even numbers in the list are {q}")

min=1
max=100
while True:
    guess= int((min+max)/2)
    print (f"is the number {guess}")
    ans = input('Say "up", "down", or "right".')
    if ans == "right":
        print("Yay me!")
    elif ans == "up":
        min = guess + 1
    elif ans == "down":
        max = guess - 1
    else:
        print("you suck")


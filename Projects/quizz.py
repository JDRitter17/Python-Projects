
while True:
    x = input("break the loop")
    if x == "break":
        break

num = int(input("â€œEnter a numberâ€"))
if num >= 5 and num <= 10:
    print("Medium")
elif num > 10:
    print("High")
else:
    print("low")

def whichIsBigger(num1, num2):
    if num1 > num2:
        return num1
    elif num1 < num2:
        return num2
    else:
        return num1

num1 = int(input("Give me a number"))
num2 = int(input("Give me another Number"))
results = whichIsBigger(num1, num2)
print(f"{results} is bigger")

alist=[]
l = [3,1,5,2,8,9,0]
for i in l:
    if i % 2 == 0:
        print(i)










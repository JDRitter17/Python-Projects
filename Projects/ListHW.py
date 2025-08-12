stuff = ['baseball', 'apple', 'kiwi', 'football']

print(len(stuff))       # Length of the list
print(stuff[3])         # Element at index 3
print(stuff[1:3])       # Slice from index 1 to 2
print(stuff[::3])       # Every 3rd element starting from index 0
print(stuff[1:5])       # Slice from index 1 to 4 (only up to end of list)

if 'kiwi' in stuff:
    print(True)
else:
    print(False)

stuff.sort()            # Sort list alphabetically
print(stuff)

planes = ['Cessna', 'Piper', 'Boeing 737Max']
states = ['Hawaii', 'Indiana']

alist = planes + states # Concatenate lists
print(alist)

blist = []
for i in planes + states:
    blist.append(i)
print(blist)

blist.reverse()         # Reverse the list in-place
print(blist)

numbers = [i for i in range(1, 1001)]  # List of numbers 1 to 1000
print(numbers)

squares = [i**2 for i in range(1, 11)] # Squares of numbers 1 to 10
print(squares)

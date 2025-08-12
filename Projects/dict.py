thisdict = {
    'scott': 46,
    'randy': 56,
    'beverly': 75
}

print(thisdict)

for name in thisdict:
    print(f"{name} is {thisdict[name]} years old")
    print(name, thisdict[name])

randy_age = thisdict['randy']
who = 'scott'

otherd = {}
for name in thisdict:
    otherd[name] = thisdict[name]

print(f"LOOK HERE {otherd}")

print(thisdict[who])
print(thisdict.keys())
print(thisdict.values())
print(randy_age)

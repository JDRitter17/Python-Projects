import re
steve = ['hello', 'hbd', 'jkl', 'mno']

for item in steve:
    if re.search(r"[AaEeIiOoUu]", item):
        print('yes')



import os
import random
import string

st1 = string.ascii_letters + string.digits + "@#$%_-"
loop = 0

os.system("cls")
while True:
    upper = 0
    lower = 0
    digit = 0
    symbol = 0
    password = ""
    for _ in range(10):
        choice = random.choice(st1)
        if choice.isupper():
            upper += 1
        elif choice.islower():
            lower += 1
        elif choice.isdigit():
            digit += 1
        else:
            symbol += 1
        password += choice
    loop += 1
    if upper >= 1 and lower >= 1 and digit >= 3 and symbol >= 2:
        break

print(f"password is {password} and took {loop} loops")

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last = number % 10
else:
    last = abs(number) % 10
    last = -l
if last == 0:
    print(f"Last digit of {number:d} is {l :d} and is 0")
elif last > 5:
    print(f"Last digit of {number:d} is {l :d} and is greater than 5")
elif last < 6:
    print(f"Last digit of {number:d} is {l :d} and is less than 6 and not 0")

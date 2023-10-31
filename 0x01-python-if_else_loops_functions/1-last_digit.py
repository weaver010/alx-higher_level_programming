#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    l = number % 10
else:
    l=abs(number)%10
    l=-l
if l== 0:
    print(f"Last digit of {number:d} is {l :d} and is 0")
elif l> 5:
    print(f"Last digit of {number:d} is {l :d} and is greater than 5")
elif l< 6:
    print(f"Last digit of {number:d} is {l :d} and is less than 6 and not 0")

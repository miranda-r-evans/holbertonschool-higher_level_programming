#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
abs_num = number
if number < 0:
    abs_num = number * -1

if abs_num % 10 > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format
          (number, abs_num % 10))
elif abs_num % 10 == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, abs_num % 10))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format
          (number, abs_num % 10))

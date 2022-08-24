#!/usr/bin/python3
import random
number = random.randit(-10000, 10000)
if number >= 0:
    mod = number % 10
else:
  mod = number % -10
if mod > 5:
  print(f"last digit of {number} is {mod} and greater than 5")
elif mod == 0:
  print(f"last digit of {number} is {mod} and is 0")
elif mod < 6:
  print(f"last digit of {number} is {mod} and is less than 6 and not 0")

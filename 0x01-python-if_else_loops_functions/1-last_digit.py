#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "The last digit of "
if number < 0:
    last_digit = (-1 * number) % 10
    last_digit = -1 * last_digit
else:
    last_digit = number % 10
if last_digit > 5:
    print("{}{:d} is {:d} and is greater than 5"
          .format(str1, number, last_digit))
elif last_digit == 0:
    print("{}{:d} is {:d} and is 0"
          .format(str1, number, last_digit))
else:
    print("{}{:d} is {:d} and is less than 6 and not 0"
          .format(str1, number, last_digit))

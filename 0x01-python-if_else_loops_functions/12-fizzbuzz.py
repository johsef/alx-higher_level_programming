#!/usr/bin/python3
def fizzbuzz():
    """Prints numbers from 1 to 100 separated by space"""
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz", end=" ")
        elif num % 5 == 0:
            print("Buzz", end=" ")
        elif num % 3 == 0:
            print("Fizz", end=" ")
        else:
            print("{:d}".format(num), end=" ")

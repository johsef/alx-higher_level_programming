#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv as ar
    if len(ar) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b")
        exit(1)
    operator = ['+', '-', '*', '/']
    op = ar[2]
    if op not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(ar[1])
    b = int(ar[3])

    if op == operator[0]:
        print("{} {} {} = {}".format(a, op, b, add(a, b)))
    elif op == operator[1]:
        print("{} {} {} = {}".format(a, op, b, sub(a, b)))
    elif op == operator[2]:
        print("{} {} {} = {}".format(a, op, b, mul(a, b)))
    else:
        print("{} {} {} = {}".format(a, op, b, div(a, b)))

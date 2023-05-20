#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    opr = sys.argv[2]
    if opr == "+":
        print("{} {} {} = {}".format(a, opr, b, add(a, b)))
    elif opr == "-":
        print("{} {} {} = {}".format(a, opr, b, sub(a, b)))
    elif opr == "*":
        print("{} {} {} = {}".format(a, opr, b, mul(a, b)))
    elif opr == "/":
        print("{} {} {} = {}".format(a, opr, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)



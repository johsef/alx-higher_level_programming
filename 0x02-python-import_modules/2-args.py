#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv as ar
    if len(ar) == 1:
        print("{:d} arguments.".format(len(ar) - 1))
    elif len(ar) == 2:
        print("{:d} argument:".format(len(ar) - 1))
        print("{:d}: {}".format(1, ar[1]))
    else:
        print("{:d} arguments:".format(len(ar) - 1))
        for i in range(1, len(ar)):
            print("{:d}: {}".format(i, ar[i]))

#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv as ar
    len_arg = len(ar)
    sum_arg = 0
    if len_arg != 1:
        for i in range(1, len_arg):
            sum_arg += int(ar[i])
    print("{}".format(sum_arg))

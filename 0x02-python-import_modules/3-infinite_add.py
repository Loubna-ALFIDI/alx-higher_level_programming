#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv) - 1
    sum = 0
    for i in range(1, n + 1):
        sum += int(argv[i])
    print("{}".format(sum))

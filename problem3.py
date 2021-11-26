#!/usr/bin/python

# DannyWeston's Solutions for the Project Euler website
# Problem (3)

import sys

from math import floor, sqrt

# argc = Argument count
# argv = Argument values
def main(argc, argv):
    ans = 0

    num = int(argv[1])

    upto = int(floor(num / 2)) + 1

    for i in range(2, upto):
        if num % i == 0:
            temp = int(num / i)
            if is_prime(temp):
                ans = temp
                break

    print(ans)

def is_prime(n):
    if n == 1: return False
    if n == 2: return True
    if n % 2 == 0: return False

    root = int(floor(sqrt(n)))

    cout = 3
    while cout < root:
        if n % cout == 0:
            return False

        cout += 2

    return True

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
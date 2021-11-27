#!/usr/bin/python

# DannyWeston's Solutions for the Project Euler website
# Problem (10)

import sys

from math import sqrt

# argc = Argument count
# argv = Argument values
def main(argc, argv):
    tally = 0
    cout = 1

    max_val = int(argv[1])
    while cout < max_val:
        if is_prime(cout):
            tally += cout

        cout += 1

    print(tally)

def is_prime(n):
    if n <= 1: return False
    if n == 2: return True

    root = int(sqrt(n)) + 1

    for i in range(2, root):
        if n % i == 0:
            return False

    return True

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
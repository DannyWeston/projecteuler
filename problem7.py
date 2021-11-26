#!/usr/bin/python

# DannyWeston's Solutions for the Project Euler website
# Problem (7)

import sys

from math import floor, sqrt

# argc = Argument count
# argv = Argument values
def main(argc, argv):
    n = int(argv[1])

    primes = []
    cout = 0
    inc = 0
    while True:
        if is_prime(inc):
            cout += 1
            primes.append(inc)

            if cout == n:
                prime = inc
                break
            
        inc += 1

    print(prime)

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
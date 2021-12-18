#!/usr/bin/python

# DannyWeston's Solutions for the Project Euler website
# Problem (#)

import sys

import math

# argc = Argument count
# argv = Argument values
def main(argc, argv):
    total = 0

    for i in list(range(1, 10000)):
        a = d(i)

        # A
        b = d(a)

        if not a == b and b == i: 
            total += i

    print(total)

def d(n):
    if n == 0 or n == 1: 
        return 0

    divisors = []

    temp = int(n / 2)
    while temp > 0:
        if n % temp == 0: divisors.append(temp)
        
        temp -= 1

    return sum(divisors)


if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
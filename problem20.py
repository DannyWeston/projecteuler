#!/usr/bin/python

# DannyWeston's Solutions for the Project Euler website
# Problem (#)

import sys
import math

# argc = Argument count
# argv = Argument values
def main(argc, argv):
    fac = str(math.factorial(100))

    total = 0
    for char in fac:
        total += int(char)

    print(total)


if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
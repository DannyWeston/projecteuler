#!/usr/bin/python

# DannyWeston's Solutions for the Project Euler website
# Problem (#)

import sys

# argc = Argument count
# argv = Argument values
def main(argc, argv):
    inc = 0

    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            inc += i

    print(inc)

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
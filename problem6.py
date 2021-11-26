#!/usr/bin/python

# DannyWeston's Solutions for the Project Euler website
# Problem (6)

import sys

# argc = Argument count
# argv = Argument values
def main(argc, argv):
    n = int(argv[1])
    print(sum_squares(n) - squares_sum(n))

def sum_squares(n):
    return int(((n * n) * ((n * n) + (2 * n) + 1)) / 4)

def squares_sum(n):
    return int(((n * n + n) * (2 * n + 1)) / 6)

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
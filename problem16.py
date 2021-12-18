#!/usr/bin/python

# DannyWeston's Solutions for the Project Euler website
# Problem (#)

import sys

# argc = Argument count
# argv = Argument values
def main(argc, argv):
    temp = str(2 ** 1000)
    print(2 ** 1000)

    val = 0

    for i in temp: val += int(i)

    print(val)

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
#!/usr/bin/python

# DannyWeston's Solutions for the Project Euler website
# Problem (#)

import sys
import math

# argc = Argument count
# argv = Argument values
def main(argc, argv):
    n = int(argv[1])

    top = math.factorial(n * 2)
    bottom = math.factorial(n) ** 2

    print(int(top / bottom))
    
if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
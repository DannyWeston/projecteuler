#!/usr/bin/python

# DannyWeston's Solutions for the Project Euler website
# Problem (9)

import sys

# argc = Argument count
# argv = Argument values
def main(argc, argv):
    ans = 0

    target = int(argv[1])

    for b in range(1, target - 1):
        found = False
        for a in range(1, b):
            c = 1000 - a - b
            if (a * a) + (b * b) == (c * c) and a + b + c == target:
                ans = a * b * c
                found = True
                break
        if found: break

    print(ans)

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
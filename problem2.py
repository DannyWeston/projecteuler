#!/usr/bin/python

# DannyWeston's Solutions for the Project Euler website
# Problem (2)

import sys

from math import sqrt, pow

# argc = Argument count
# argv = Argument values
def main(argc, argv):
    upto = int(argv[1])

    total = 2
    i = 0
    val = fib(i)
    while val < upto:
        total += val

        i += 3
        val = fib(i)

    print(total)

fib_cache = {0:0, 1:1, 2:1}
def fib(n):
    a = b = -1

    if n in fib_cache: return fib_cache[n]
    
    if n - 1 in fib_cache: a = fib_cache[n - 1]
    else: a = fib(n - 1)
    
    if n - 2 in fib_cache: b = fib_cache[n - 2]
    else: b = fib(n - 2)

    fib_cache[n] = a + b
    return a + b

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
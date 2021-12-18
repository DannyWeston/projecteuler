#!/usr/bin/python

# DannyWeston's Solutions for the Project Euler website
# Problem (#)

import sys

import matplotlib.pyplot as plt

# argc = Argument count
# argv = Argument values
def main(argc, argv):

    result = None
    max = 0

    upto = 1000000

    for i in list(range(1, upto + 1)):
        c = collatz(i)

        if max < c: 
            max = c
            result = i

    print(result)

calced = { 1 : 1 }

def collatz(n):
    count = 0
    temp = n

    while temp >= n:
        if temp in calced:
            calced[n] = count + calced[temp]
            return calced[n]

        if temp % 2 == 0:
            temp /= 2
            count += 1
        else:
            temp = ((temp * 3) + 1) / 2
            count += 2

    calced[n] = count + calced[temp]
    return calced[n]

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
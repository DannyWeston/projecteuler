#!/usr/bin/python

# DannyWeston's Solutions for the Project Euler website
# Problem (5)

import sys

# argc = Argument count
# argv = Argument values
def main(argc, argv):
    list = range(3, 21)
    filtered = []

    for i in list:
        for j in list:
            if j == i: continue

            if j % i == 0: break

        else: filtered.append(i)

    start = 1
    for i in filtered:
        start *= i

    last = start
    while True:

        for x in filtered:
            temp = int(last / x)

            if all_factors(temp, filtered):
                last = temp
                break
        else: break
    
    print(last)
                
def all_factors(n ,factors):
    for x in factors:
        if n % x != 0:
            return False

    return True

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
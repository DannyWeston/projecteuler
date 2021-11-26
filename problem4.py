#!/usr/bin/python

# DannyWeston's Solutions for the Project Euler website
# Problem (4)

import sys

# argc = Argument count
# argv = Argument values
def main(argc, argv):
    max = 0
    for i in range(1000, 100, -1):
        for j in range(1000, 100, -1):
            ans = i * j
            if palindrome(ans):
                if ans > max: 
                    print((max, ans))
                    max = ans

    print(max)

def palindrome(n):
    temp = str(n)
    length = len(temp)
    
    if length % 2 == 0:
        half = int(length / 2)
        a = temp[0:half]
        b = temp[half:length]

        return a[::-1] == b
    else:
        half = int(length / 2)
        a = temp[0:half]
        b = temp[half + 1:length]

        return a[::-1] == b

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
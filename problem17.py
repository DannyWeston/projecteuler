#!/usr/bin/python

# DannyWeston's Solutions for the Project Euler website
# Problem (#)

import sys

# argc = Argument count
# argv = Argument values
def main(argc, argv):
    cout = 0
    for i in list(range(1, 1001)):
        cout += num_to_letters(i)

    print(cout)

vals = {
    1 : 3,
    2 : 3,
    3 : 5,
    4 : 4,
    5 : 4,
    6 : 3,
    7 : 5,
    8 : 5,
    9 : 4,
    10 : 3,
    11 : 6,
    12 : 6,
    13 : 8,
    14 : 8,
    15 : 7, 
    16 : 7,
    17 : 9,
    18 : 8,
    19 : 8,
    20 : 6,
    30 : 6,
    40 : 5,
    50 : 5,
    60 : 5,
    70 : 7,
    80 : 6,
    90 : 6,
    100 : 7,
}   

def num_to_letters(n):
    num = n

    chars = 0

    # Thousand
    if n == 1000: return 11

    # Hundreds
    if num >= 100:
        hundreds = int(num / 100)
        
        chars += vals[hundreds] + vals[100]

        num -= (hundreds * 100)

        # Other stuff so add "and"
        if num > 0: chars += 3
        else: return chars
      
    # Number 0 <= x <= 99

    # 0 or 1 in tens column
    if num < 20: return vals[num] + chars

    tens = int(num / 10) * 10

    # Add tens column
    chars += vals[tens]

    # Add digits column
    num -= tens 

    if num > 0: chars += vals[num]
    
    return chars

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        digits = list(map(int,f.read()))
        print(sum(map(lambda x: x[0],filter(lambda x: x[0]==x[1],zip(digits, digits[1:]+digits[0:1])))))

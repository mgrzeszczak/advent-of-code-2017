#!/usr/bin/env python3

import sys
import math

if __name__ == '__main__':
    with open('input') as f:
        l = list(map(int,f.read().split('\n')))
        pos = 0
        steps = 0
        while 0 <= pos < len(l):
            d = l[pos]
            if d >= 3:
                l[pos] = l[pos]-1
            else:
                l[pos] = l[pos]+1
            pos += d
            steps += 1
        print(steps)

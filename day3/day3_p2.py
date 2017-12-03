#!/usr/bin/env python3

import sys
import time
from itertools import islice
import matplotlib.pyplot as plt
import numpy as np

def neighbors(x,y):
    yield (x,y-1)
    yield (x-1,y-1)
    yield (x-1,y)
    yield (x-1,y+1)
    yield (x,y+1)
    yield (x+1,y+1)
    yield (x+1,y)
    yield (x+1,y-1)

def positions():
    sides = 0
    cw = 3
    cp = 2

    dx = 0
    dy = -1

    cx = 1
    cy = 0
    while True:
        yield (cx, cy)
        cx += dx
        cy += dy
        cp += 1
        if cp == cw:
            sides += 1
            cp = 1
            if sides == 4:
                yield(cx, cy)
                cx += 1
                sides = 0
                cw += 2
                cp = 2
            if sides == 0:
                dx = 0
                dy = -1
            elif sides == 1:
                dx = -1
                dy = 0
            elif sides == 2:
                dx = 0
                dy = 1
            else:
                dx = 1
                dy = 0


if __name__ == '__main__':
    N = int(sys.argv[1])
    size = 1
    while True:
        M = np.zeros((size+1,size+1))
        n = int(size/2)
        M[n,n] = 1
        print('Size: {}x{}'.format(size+1,size+1))
        for off in positions():
            p = (n+off[0], n+off[1])
            if p[0]<1 or p[0] >= size or p[1]<1 or p[1]>=size:
                break
            v = sum(map(lambda x: M[x[0],x[1]],neighbors(p[0],p[1])))
            M[p[0],p[1]] = v
            if v > N:
                print(int(v))
                sys.exit(0)
        size*=2

#!/usr/bin/env python3

import sys
import math


def dist(n, x, closest):
    return x + abs(closest - x - n)


if __name__ == '__main__':
    n = int(sys.argv[1])
    x = math.ceil(math.sqrt(n) / 2 - 0.5)
    y = 2 * x + 1
    yp = y - 2
    start = yp * yp + 1
    ru = start + yp
    lu = ru + yp + 1
    lb = lu + yp + 1
    rb = lb + yp + 1
    d = 0
    if ru > n:
        d = dist(n, x, ru)
    elif lu > n:
        d = dist(n, x, lu)
    elif lb > n:
        d = dist(n, x, lb)
    else:
        d = dist(n, x, rb)
    print(d)

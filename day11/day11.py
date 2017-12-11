#!/usr/bin/env python3

import sys
import re
import os
from functools import reduce
import numpy as np


def flatten(sequence: iter, func: callable = lambda x: x):
    return reduce(lambda res, x: res + func(x), sequence, [])


def parse(regex: str, text: str, func: callable = lambda x: x):
    r = re.search(regex, text)
    groups = r.groups()
    return func(groups)


def to_hex(i: int):
    return f'{i:02X}'


if __name__ == '__main__':
    with open('input') as f:
        steps = f.read().split(',')
        dists = []
        x = 0
        y = 0
        z = 0
        # https://www.redblobgames.com/grids/hexagons/ - hex grid explained
        for d in steps:
            if d == "n":
                y -= 1
                x += 1
            elif d == "s":
                y += 1
                x -= 1
            elif d == "ne":
                y -= 1
                z += 1
            elif d == "sw":
                y += 1
                z -= 1
            elif d == "nw":
                x += 1
                z -= 1
            elif d == "se":
                z += 1
                x -= 1
            dists.append((abs(x) + abs(y) + abs(z)) / 2)
        print((abs(x) + abs(y) + abs(z)) / 2)
        print(max(dists))

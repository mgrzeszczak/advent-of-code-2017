#!/usr/bin/env python3

import sys
import re
import os
from functools import reduce


def flatten(sequence, func=lambda x: x):
    return reduce(lambda r, x: r + func(x), sequence, [])


def parse(regex, text, func=lambda x: x):
    r = re.search(regex, text)
    groups = r.groups()
    return func(groups)


def to_hex(i):
    return f'{i:02X}'


if __name__ == '__main__':
    with open('input') as f:
        lengths = list(map(ord, f.read())) + [17, 31, 73, 47, 23]
        knot_hash = list(range(256))
        skip = 0
        position = 0
        size = 256
        for r in range(64):
            for l in lengths:
                if position + l <= size:
                    knot_hash = knot_hash[0:position] + knot_hash[position:position + l][::-1] + knot_hash[
                                                                                                 position + l:]
                else:
                    part = (knot_hash[position:] + knot_hash[0:l - (size - position)])[::-1]
                    l1 = size - position
                    l2 = l - (size - position)
                    knot_hash = part[l1:l1 + l2] + knot_hash[l - (size - position):position] + part[0:l1]
                position = (position + l + skip) % size
                skip += 1
        dense_hash = [reduce(lambda a, b: a ^ b, knot_hash[i * 16:i * 16 + 16]) for i in range(16)]
        print(reduce(lambda a, b: a + f'{b:02X}', dense_hash, ''))

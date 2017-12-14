#!/usr/bin/env python3

import sys
import re
import os
from functools import reduce


def flatten(sequence: iter, func: callable = lambda x: x):
    return reduce(lambda res, x: res + func(x), sequence, [])


def parse(regex: str, text: str, func: callable = lambda x: x):
    r = re.search(regex, text)
    groups = r.groups()
    return func(groups)


def to_hex(i: int):
    return f'{i:02X}'


def knot_hash(input):
    lengths = list(map(ord, input)) + [17, 31, 73, 47, 23]
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
    return reduce(lambda a, b: a + f'{b:02X}', dense_hash, '')


import numpy as np


def directions(pos):
    x, y = pos
    if x > 0:
        yield (x - 1, y)
    if x < 127:
        yield (x + 1, y)
    if y < 127:
        yield (x, y + 1)
    if y > 0:
        yield (x, y - 1)


def search_block(pos, mat, number):
    x, y = pos
    if mat[x, y] != 1:
        return False
    mat[x, y] = number
    for d in directions(pos):
        search_block(d, mat, number)
    return True


if __name__ == '__main__':
    input = 'jxqlasbh'
    count = 0
    mat = np.zeros((128, 128))

    for i in range(128):
        hash = knot_hash(input + "-" + str(i))
        bits = reduce(lambda a, b: a + b, map(lambda c: format(int(c, 16), '0>4b'), list(hash)), '')
        row = list(map(lambda x: ord(x) - ord('0'), list(bits)))
        count += sum(row)
        mat[i] = np.array(row)

    print(count)

    blockNumber = 2

    for x in range(128):
        for y in range(128):
            pos = (x, y)
            if search_block(pos, mat, blockNumber):
                blockNumber += 1
    #print(mat)
    print(blockNumber - 2)

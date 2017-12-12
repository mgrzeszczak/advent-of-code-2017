#!/usr/bin/env python3

import sys
import re
import os
from functools import reduce
import numpy as np


def flatten(sequence, func=lambda x: x):
    return reduce(lambda res, x: res + func(x), sequence, [])


def parse(regex, text, func=lambda x: x):
    r = re.search(regex, text)
    groups = r.groups()
    return func(groups)


def to_hex(i):
    return f'{i:02X}'


def find_all(current, channels, withZero):
    for c in channels[current]:
        withZero.append(c)
    for c in channels:
        find_all(c, channels, withZero)


def find_group(index, data):
    elems = {index}
    queue = [index]
    while len(queue):
        e = queue[0]
        queue = queue[1:]
        for v in data:
            if v[0] == e:
                for n in v[1]:
                    if n not in elems:
                        elems.add(n)
                        queue.append(n)
                break
    return elems


if __name__ == '__main__':
    with open('input') as f:
        data = f.read().split('\n')
        data = list(map(lambda x: [int(x[0]), list(map(int, x[1].split(', ')))], map(lambda x: x.split(' <-> '), data)))
        # part 1
        print(len(find_group(0, data)))
        # part 2
        copy = list(data)
        sets = []
        current = set()
        while len(copy):
            e = copy[0]
            index = e[0]
            group = find_group(index, copy)
            sets.append(group)
            copy = list(filter(lambda x: x[0] not in group, copy))
        print(len(sets))

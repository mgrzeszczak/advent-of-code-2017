#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        count = 0
        for line in f:
            words = list(map(lambda x: ''.join(sorted(x)),line[:-1].split(' ')))
            if len(set(words)) == len(words):
                count += 1
        print(count)

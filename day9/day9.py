#!/usr/bin/env python3

import sys
import re
import os

def parse_line(line):
    r = re.search(r'(.*)', line)
    groups = r.groups()
    return groups

if __name__ == '__main__':
    with open('input') as f:
        rules = f.read().split('\n')
        totalscore = 0
        removed = 0
        for rule in rules:
            depth = 0
            ignore = False
            score = 0
            inGarbage = False
            for c in rule:
                if ignore:
                    ignore = False
                    continue

                if inGarbage:
                    if c =='!':
                        ignore = True
                    elif c == '>':
                        inGarbage = False
                    else:
                        removed +=1
                else:
                    if c == '{':
                        depth += 1
                    elif c == '}':
                        score += depth
                        depth -= 1
                    elif c == '<':
                        inGarbage = True
            totalscore += score
        print(totalscore)
        print(removed)

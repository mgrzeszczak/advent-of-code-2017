#!/usr/bin/env python3

import sys
import re
import os
from aocd import get_data

def parse_line(line):
    r = re.search(r'(.*)', line)
    groups = r.groups()
    return groups

if __name__ == '__main__':
    print(get_data())

#!/usr/bin/env python3
import re
import sys

def single(program):
    r = re.search(r'(\w+) \((\d+)\)( -> ((\w+, )*\w+))?', program)
    return [r.groups()[0], int(r.groups()[1]), r.groups()[3].split(', ') if r.groups()[3] else None]

def calc_balance(root, tmap):
    if not root[2]:
        return root[1]
    subtrees = list(map(lambda x: tmap[x], root[2]))
    return root[1]+sum(map(lambda x: calc_balance(x, tmap),subtrees))

def find_unique(values):
    s = sorted(values)
    if s[0] == s[1] == s[-1]:
        return (False,0)
    elif s[0] == s[1]:
        return (True,s[-1])
    else:
        return (True,s[0])

def check_balance(root, tmap):
    diff = None
    while True:
        if root[2] == None:
            print(root[1]-diff)
            sys.exit(0)
        l = list(map(lambda x: tmap[x],root[2]))
        balances = list(map(lambda x: calc_balance(x,tmap), l))
        found, unique = find_unique(balances)
        if not found:
            print(root[1]-diff)
            sys.exit(0)
        else:
            index = balances.index(unique)
            diff = unique- (balances[0] if index != 0 else balances[-1])
            root = l[index]
            

if __name__ == '__main__':
    with open('input') as f:
        data = f.read().split('\n')
        data = list(map(single,data))
        depending = []
        for d in data:
            if d[2]:
                for c in d[2]:
                    depending.append(c)
        tmap = {}
        root = None
        for d in data:
            tmap[d[0]] = d
            if d[0] not in depending:
                root=d
                print(root[0])

        check_balance(root,tmap) 

        

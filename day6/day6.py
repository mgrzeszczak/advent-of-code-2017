#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    with open('input') as f:
        data = list(map(int,f.read()[0:-1].split('\t')))
        states = [list(data)]
        when = {}
        when[','.join(map(str,data))] = 0
        #when = {(','.join(data)) : 0}
        size = len(data)
        steps = 0
        while True:
            i = data.index(max(data))
            val = data[i]
            data[i] = 0
            while val > 0:
                i = (i+1)%size
                data[i] += 1
                val -=1
            steps += 1
            if data in states:
                print(steps,steps-when[','.join(map(str,data))])
                sys.exit(0)
            else:
                states.append(list(data))
                when[','.join(map(str,data))] = steps

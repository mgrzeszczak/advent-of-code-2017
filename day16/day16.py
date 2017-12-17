#!/usr/bin/env python3

def dance(dancers, moves):
    for m in moves:
        if m[0] == 's':
            count = int(m[1:])
            dancers = dancers[-count:] + dancers[:-count]
        elif m[0] == 'x':
            a, b = m[1:].split('/')
            a = int(a)
            b = int(b)
            dancers[a], dancers[b] = dancers[b], dancers[a]
        elif m[0] == 'p':
            x, y = m[1:].split('/')
            a, b = dancers.index(x), dancers.index(y)
            dancers[a], dancers[b] = dancers[b], dancers[a]
    return dancers


def dance_times(dancers, moves, repeat):
    step = 0
    known = {''.join(dancers): 0}
    positions = {0: ''.join(dancers)}
    while step < repeat:
        dancers = dance(dancers, moves)
        step += 1
        key = ''.join(dancers)
        if key in known:
            count = step - known[key]
            return positions[repeat % count]
        else:
            known[key] = step
            positions[step] = key


def parse_data():
    with open('input') as f:
        return f.read().split(',')


if __name__ == '__main__':
    data = parse_data()
    dancers = list(map(lambda x: chr(ord('a') + x), range(16)))
    print('Part1: '+''.join(dance(dancers, data)))
    print('Part2: '+dance_times(dancers, data, 1000 * 1000 * 1000))

#!/usr/bin/env python3


def blocks(height, time):
    offset = 2 * height - 2
    return time * height if time % offset == 0 else 0


if __name__ == '__main__':
    lines = [line.split(': ') for line in open('input').read().split('\n')]
    heights = {int(pos): int(height) for pos, height in lines}
    print(sum(map(lambda col: blocks(heights[col], col), heights)))

    delay = 0
    while True:
        if sum(map(lambda col: blocks(heights[col], col+delay), heights)) == 0:
            print(delay)
            break
        else:
            delay += 1
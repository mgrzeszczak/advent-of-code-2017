#!/usr/bin/env python3


def generate(start, factor, multiplyof):
    prev = start
    while True:
        prev *= factor
        prev %= 2147483647
        if prev % multiplyof == 0:
            yield prev


def lowest_16_bits(value):
    return '{0:032b}'.format(value)[16:]


if __name__ == '__main__':
    startA = 512
    startB = 191

    genA = generate(startA, 16807,4)
    genB = generate(startB, 48271,8)
    
    count = 0
    for i in range(5*1000*1000):
        if i % 1000 == 0:
            print(i)
        a = next(genA)
        b = next(genB)
        if lowest_16_bits(a) == lowest_16_bits(b):
            count += 1
    print(count)



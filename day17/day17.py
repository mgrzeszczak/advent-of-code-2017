import sys


if __name__ == '__main__':
    steps = 370

    # part 2
    length = 1
    position = 0
    second = None
    for i in range(50*1000*1000):
        position += steps
        position %= length
        if position == 0:
            second = (i+1)
        length += 1
        position += 1
        if i % 100000 == 0:
            print(i)
    print(second)

    # part 1
    # buffer = [0]
    # position = 0
    #for i in range(5 * 1000 * 1000):
    #    if i % 10000 == 0:
    #        print(i)
    #    position += steps
    #    position %= len(buffer)
    #    buffer.insert(position + 1, i + 1)
    #    position = (position + 1) % len(buffer)

    #print(buffer[(buffer.index(0) + 1) % len(buffer)])

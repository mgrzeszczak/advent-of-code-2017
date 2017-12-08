
import re
import sys

def single(program):
    #s dec 63 if obo >= -4125
    r = re.search(r'(\w+) (dec|inc) (-?\d+) if (\w+) (.*)', program)
    print(r)
    return [r.groups()[0], (1 if r.groups()[1] == "inc" else -1)*int(r.groups()[2]) , r.groups()[3], r.groups()[4]]

if __name__ == '__main__':
    with open('input') as f:
        data = f.read().split('\n')
        data = list(map(single, data))
        print(data)
        registers = {}
        maxheld = 0
        for d in data:
            registers[d[0]] = 0
        for d in data:
            if eval(str(registers[d[2]])+d[3]):
                registers[d[0]] = registers[d[0]] + d[1]
                if registers[d[0]] > maxheld:
                    maxheld = registers[d[0]]
        max = 0
        for d in data:
            if registers[d[0]] > max:
                max = registers[d[0]]
        print(max, maxheld)
        
            
            
        

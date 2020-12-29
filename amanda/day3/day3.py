import sys
import functools
from typing import List

def part1(strings: List[str]) ->None:
    x = 0
    y = 0 
    count = 0

    while y < len(strings):
        line = strings[y] 
        tri = line[x % len(line)] 
        x += 3
        y += 1
        if tri == '#':
            count += 1

    print(count)

def part2(strings: List[str]) ->None:
    t = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    result = []

    for i in t:
        x = 0
        y = 0 
        count = 0
        while y < len(strings):
            line = strings[y] 
            tri = line[x % len(line)] 
            x += i[0]
            y += i[1]
            if tri == '#':
                count += 1  
        result.append(count)
        print(count)
    print(result)
    
    total = functools.reduce(lambda a,b: a *b, result)
    print(total)

if __name__ == '__main__':
    myinput = sys.stdin.read().split("\n")
    part1(myinput)
    part2(myinput)
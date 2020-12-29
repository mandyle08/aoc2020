import re 
import sys
from typing import List

def part1(strings: List[str]) ->None:
    counter = 0 
    for string in strings:
        m = re.fullmatch(r'(\d+)-(\d+) ([a-z]): (.*)', string)
        assert m is not None
        low = int(m[1])
        high = int(m[2])
        letter = m[3]
        password = m[4]

        if low <= password.count(letter) <= high:
            counter += 1

    print(counter)    

def part2(strings: List[str]) ->None:
    counter = 0 
    for string in strings:
        m = re.fullmatch(r'(\d+)-(\d+) ([a-z]): (.*)', string)
        assert m is not None
        low = int(m[1])
        high = int(m[2])
        letter = m[3]
        password = m[4]

        if password[low-1].count(letter) + password[high-1].count(letter) == 1:
            counter +=1 
    print(counter)

if __name__ == '__main__':
    myinput = sys.stdin.read().split("\n")
    part1(myinput)
    part2(myinput)


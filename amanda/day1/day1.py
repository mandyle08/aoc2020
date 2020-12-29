#! /usr/bin/python3
import sys
from typing import List

def part1(numbers: List[int]) -> None:
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == 2020:
                print(numbers[i] * numbers[j])
                return

def part2(numbers: List[int]) -> None:
    numbers = sorted(numbers)

    for i in range(0, len(numbers)):
        j = i + 1
        k = len(numbers) - 1

        while j < k:
            first  = numbers[i]
            second = numbers[j]
            third  = numbers[k]
            if (first + second + third) > 2020:
                k -= 1
            elif (first + second + third) < 2020:
                j += 1
            else:
                print(first * second * third)
                return

if __name__ == '__main__':
    myinput = sys.stdin.read().split("\n")
    myinput = list(map(lambda x: int(x), myinput))
    part1(myinput)
    part2(myinput)


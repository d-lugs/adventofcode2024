# DAY 3

import re

def main():
    input = open("input.txt","r").read()

    print(f"part 1: {part1(input)}")
    print(f"part 2: {part2(input)}")

def part1(input):
    regex = r"(?<!\w)(mul\(\d{1,3},\d{1,3}\))"
    matches = re.findall(regex, input)

    total = 0
    for string in matches:
        match = re.search(r"mul\((?P<first>\d{1,3}),(?P<second>\d{1,3})\)",string)
        first = int(match.group('first'))
        second = int(match.group('second'))
        total += first * second
    return total

def part2(input):
    regex = r"((?<!\w)mul\(\d{1,3},\d{1,3}\)|don't|do)"
    matches = re.findall(regex, input)

    total = 0
    condition = True
    for string in matches:
        if string == "don't":
            condition = False
            continue
        elif string == "do":
            condition = True
            continue

        if condition:
            match = re.search(r"mul\((?P<first>\d{1,3}),(?P<second>\d{1,3})\)",string)
            first = int(match.group('first'))
            second = int(match.group('second'))
            total += first * second
    
    return total

main()
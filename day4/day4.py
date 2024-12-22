# DAY 4
# find all instances of 'xmas' in the word search provided in input.txt
# horizontal, vertical, diagonal and backwards (for all directions)

import re

def main():
    input = open("input.txt","r")
    lines = input.read().splitlines()

    horizontal = findHorizontal(lines)

    array = []
    for line in lines:
        array.append(list(line))

    print(horizontal)

# each function should return a count of all instances of 'xmas' both forwards and backwards

def findHorizontal(lines):
    regex_f = r"(XMAS)"
    regex_b = r"(SAMX)"
    count = 0
    for line in lines:
        count += len(re.findall(regex_f, line)) + len(re.findall(regex_b, line))
    return count

def findVertical(array):
    return 0

def findDiagonal(array):
    return 0

main()

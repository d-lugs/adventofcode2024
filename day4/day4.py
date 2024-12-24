# DAY 4
# find all instances of 'xmas' in the word search provided in input.txt
# horizontal, vertical, diagonal and backwards (for all directions)

import re

def main():
    input = open("input.txt","r")
    lines = input.read().splitlines()

    horizontals = findHorizontal(lines)

    array = []
    for line in lines:
        if list(line) != []:
            array.append(list(line))

    verticals = findVertical(array)

    diagonals = findDiagonal(array)

    total = horizontals + verticals + diagonals

    print(total)

# each function should return a count of all instances of 'xmas' both forwards and backwards

def findHorizontal(lines):
    regex_f = r"(XMAS)"
    regex_b = r"(SAMX)"
    count = 0
    for line in lines:
        count += len(re.findall(regex_f, line)) + len(re.findall(regex_b, line))
    return count

def findVertical(array):
    transposed = [[row[i] for row in array] for i in range(len(array[0]))]
    lines = []
    for row in transposed:
        line = ""
        for char in row:
            line += char
        lines.append(line)
    count = findHorizontal(lines)
    return count

def findDiagonal(array):
    col = len(array[0])
    row = len(array)

    fdiag = [[] for _ in range(col + row - 1)]
    bdiag = [[] for _ in range(len(fdiag))]
    min_bdiag = -row + 1

    for x in range(col):
        for y in range(row):
            fdiag[x+y].append(array[y][x])
            bdiag[x-y-min_bdiag].append(array[y][x])

    def getLines(diag):
        lines = []
        for row in diag:
            line = ""
            for char in row:
                line += char
            lines.append(line)
        return lines

    fdiag_lines = getLines(fdiag)
    bdiag_lines = getLines(bdiag)

    count = 0
    count += findHorizontal(fdiag_lines) + findHorizontal(bdiag_lines)

    return count

main()

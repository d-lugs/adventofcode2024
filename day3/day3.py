import re

input = open("input.txt","r")

regex = r"(?<!\w)(mul\(\d{1,3},\d{1,3}\))"
matches = re.findall(regex, input.read())

total = 0
for string in matches:
    match = re.search(r"mul\((?P<first>\d{1,3}),(?P<second>\d{1,3})\)",string)
    first = int(match.group('first'))
    second = int(match.group('second'))
    total += first * second

print(total)

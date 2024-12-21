# read input file
input = open("./input.txt","r")
lines = input.readlines()

# determine if each "report" (line) is safe or not, count number of safe reports
# safe = all "levels" (numbers are increasing/decreasing by 1, 2, or 3
count = 0
for l in lines:
    # determine if report is in order
    report = []
    for level in l.split(): report.append(int(level))
    if report == sorted(report): pass
    elif report == sorted(report, reverse=True): pass
    else: continue
    # determine if each level in report is safe
    safe = False
    for i in range(len(report)):
        if i < len(report)-1:
            if abs(report[i]-report[i+1]) > 3: continue
print(count)

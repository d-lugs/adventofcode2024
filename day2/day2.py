# DAY 2
# determine if each "report" (line) is safe or not, count number of safe reports
# safe = all "levels" (numbers are increasing/decreasing by 1, 2, or 3

def main():
    input = open("input.txt","r")
    lines = input.read().splitlines()

    count = 0
    for line in lines:
        report = []
        for level in line.split():
            report.append(int(level))

        gradual = is_gradual(report,1)
        in_order = check_order(report,1)
        in_order_reverse = check_order(list(reversed(report)),1)

        if gradual and (in_order or in_order_reverse):
            count += 1

    print(count)

def is_gradual(report, tolerance):
    gradual = False
    diffs = []
    for i in range(len(report)):
        diff = 0
        try:
            diff = report[i+1] - report[i]
            diffs.append(diff)
            if abs(diff) < 4:
                gradual = True
            else:
                if tolerance == 0:
                    gradual = False
                    break
                else:
                    tolerance -= 1
        except IndexError:
            pass
    if 0 in diffs: gradual = False
    return gradual

def check_order(report, tolerance):
    # old solution for part 1
    # in_order = False
    # if report == sorted(report):
    #     in_order = True
    # elif report == sorted(report, reverse=True):
    #     in_order = True
    # else:
    #     in_order = False

    in_order = True
    for i in range(len(report)):
        try:
            if report[i] < report[i+1]:
                pass
            else:
                if tolerance == 0:
                    in_order = False
                    break
                else:
                    tolerance -= 1
        except IndexError:
            pass
    
    print(report, in_order)

    return in_order 

def is_safe(report, tolerance):
    safe = False
    diffs = []
    for i in range(len(report)):
        diff = 0
        try:
            diff = report[i+1] - report[i]
            diffs.append(diff)
            if abs(diff) < 4:
                safe = True
            else:
                if tolerance == 0:
                    safe = False
                    break
                else:
                    tolerance -= 1
        except IndexError:
            pass
    if 0 in diffs: safe = False
    return safe

main()

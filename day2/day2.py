# DAY 2
# determine if each "report" (line) is safe or not, count number of safe reports
# safe = all "levels" (numbers are increasing/decreasing by 1, 2, or 3

def main():
    input = open("input.txt","r")
    lines = input.read().splitlines()

    count1 = 0
    count2 = 0
    for line in lines:
        report = []
        for level in line.split():
            report.append(int(level))

        gradual = is_gradual(report)
        in_order = check_order(report)

        if gradual and in_order:
            count1 += 1
            count2 += 1
        elif with_dampener(report):
            count2 += 1

    print(f"without dampener: {count1}")
    print(f"with dampener: {count2}")

def is_gradual(report):
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
                safe = False
                break
        except IndexError:
            pass
    
    if 0 in diffs: 
        safe = False

    return safe

def check_order(report):
    safe = False

    if report == sorted(report):
        safe = True
    elif report == sorted(report, reverse=True):
        safe = True
    else:
        safe = False

    return safe

def with_dampener(report):
    safe = False
    for i in range(len(report)):
        temp_report = [i for i in report]
        del temp_report[i]
        
        gradual = is_gradual(temp_report)
        in_order = check_order(temp_report)

        if gradual and in_order:
            safe = True

    return safe

main()

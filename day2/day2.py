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

        print(f"{str(report):<40}", end=" ")

        gradual = is_gradual(report)
        in_order = check_order(report)

        # if not gradual: print("not gradual", end=" ")
        # if not in_order: print("not in order", end=" ")

        if gradual and in_order:
            # print("safe", end=" ")
            count += 1

        print()

    print(count)

def is_gradual(report):
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
                gradual = False
                break
        except IndexError:
            pass
    if 0 in diffs: gradual = False
    print(f"{str(diffs):<40}", end=" ")
    return gradual

def check_order(report):
    in_order = False
    if report == sorted(report):
        in_order = True
    elif report == sorted(report, reverse=True):
        in_order = True
    else:
        in_order = False
    return in_order

main()

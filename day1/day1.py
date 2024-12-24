# DAY 1.1

# read input file
input = open("./input.txt", "r")
lines = input.readlines()

# sort left and right lists from smallest to largest
left = []
right=[]
for i in range(len(lines)):
    l = lines[i].split()
    left.append(int(l[0]))
    right.append(int(l[1]))
left.sort()
right.sort()

# find total differences between each pair
diff_total = 0
for i in range(len(lines)):
    diff_total += abs(left[i]-right[i])
print(diff_total)


# DAY 1.2

score = 0
for i in left:
    count = 0
    for n in right:
        if i == n:
            count += 1
    score += i * count
print(score)
safe = 0

reports = []
with open("input.txt", "r") as f:
    reports = f.readlines()

for report in reports:
    levels = report.split(" ")
    levels[-1] = levels[-1].strip()
    levels = list(map(int, levels))

    is_increasing = levels[0] < levels[1]

    ptr1 = 0
    ptr2 = 1
    violations = 0
    while ptr2 < len(levels):
        diff = levels[ptr1] - levels[ptr2]

        # check if same direction and correct diff
        if is_increasing and diff > 0:
            violations += 1
        if not is_increasing and diff < 1:
            violations += 1 

        # check if diff greater than safe
        abs_diff = abs(diff)
        if abs_diff < 1 or abs_diff > 3:
            violations += 1

        ptr1 += 1
        ptr2 += 1

    if violations - 1 <= 0:
        safe += 1

print(safe)

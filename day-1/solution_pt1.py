list1 = []
list2 = []

with open("input.txt", "r") as f:
    for line in f:
        output = line.split("   ")
        list1.append(int(output[0].strip()))
        list2.append(int(output[1].strip()))

list1.sort()
list2.sort()

total_diff = 0
for idx in range(0, len(list1)):
    total_diff += abs(list1[idx] - list2[idx])

print(total_diff)


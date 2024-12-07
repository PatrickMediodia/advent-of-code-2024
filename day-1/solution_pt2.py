list1 = []

list2 = []
dict2 = {}

# get inputs
with open("input.txt", "r") as f:
    for line in f:
        output = line.split("   ")

        # build first list
        list1.append(int(output[0].strip()))
        
        # build second list
        second_input = int(output[1].strip())
        list2.append(second_input)

        # build second dictionary        
        if second_input in dict2:
            dict2[second_input] += 1
        else:
            dict2[second_input] = 1

similarity = 0
for val in list1:
    if not val in dict2:
        continue
    similarity += val * dict2[val]

print(similarity)

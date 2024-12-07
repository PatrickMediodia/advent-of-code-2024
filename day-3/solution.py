import re

inputs = []
with open("input.txt", "r") as f:
    inputs = f.readlines()

regex_pattern = r"mul\(\d{1,3},\d{1,3}\)"
output = 0

for input in inputs:
    matches = re.findall(regex_pattern, input)
    for match in matches:
        new_string = match[4:len(match)-1]
        numbers = new_string.split(",")
        output += int(numbers[0]) * int (numbers[1])

print(output)

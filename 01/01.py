import re
file = open("input.txt", "r")


noChar = []
for c in file:
    noChar.append(re.sub(r'[a-zA-Z\n]', "", c))

ints = []
for i in noChar:
    ints.append(int(i[0] + i[-1]))


print(sum(ints))
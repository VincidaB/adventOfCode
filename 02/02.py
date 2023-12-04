import re


f = open("input.txt")

sumIds = 0

for x in f:
    print(x)
    reds =  re.findall(r'([0-9]+) red',x)
    greens =  re.findall(r'([0-9]+) green',x)
    blues =  re.findall(r'([0-9]+) blue',x)


    reds = [int(i) for i in reds]
    greens = [int(i) for i in greens]
    blues = [int(i) for i in blues]

    if max(reds) > 12:
        continue
    if max(greens) > 13:
        continue
    if max(blues) > 14:
        continue
    s = re.findall(r'Game ([0-9]+)', x)
    sumIds += int(s[0])
    
print(sumIds)
import re


f = open("input.txt")

sumPower = 0

for x in f:
    print(x)
    reds =  re.findall(r'([0-9]+) red',x)
    greens =  re.findall(r'([0-9]+) green',x)
    blues =  re.findall(r'([0-9]+) blue',x)


    reds = [int(i) for i in reds]
    greens = [int(i) for i in greens]
    blues = [int(i) for i in blues]

    mr = max(reds)
    mg = max(greens)
    mb = max(blues)



    power = mr*mg*mb
    
    sumPower += power
    
print(sumPower)
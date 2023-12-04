import re
file = open("input.txt", "r")
#file = open("inputTest.txt", "r")


noChar = []
filechanged = ""

# substitution of all worlds
for x in file:
    #letters are sometimes added to complete words that are before or after in 
    # the string, but that are tested later in the program
    newline = re.sub(r'one', "o1e", x)
    newline = re.sub(r'two', "t2", newline)
    newline = re.sub(r'three', "t3", newline)
    newline = re.sub(r'four', "4", newline)
    newline = re.sub(r'five', "5", newline)
    newline = re.sub(r'six', "6", newline)
    newline = re.sub(r'seven', "7", newline)
    newline = re.sub(r'eight', "8", newline)
    newline = re.sub(r'nine', "9", newline)
    
    
    
    noChar.append(re.sub(r'[a-zA-Z\n]', "", newline))
    

ints = []
for i in noChar:
    ints.append(int(i[0] + i[-1]))

print(ints)

print(sum(ints))
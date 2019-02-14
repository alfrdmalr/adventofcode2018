import sys

rawInput = sys.stdin.readlines()
input = []
for line in rawInput:
    input.append(line.strip())

answer = ""

for line in input:
    if len(answer) != 0:
        break
    for idString in input:
        differenceCount = 0
        tentativeString = ""
        for i in range(0, len(idString)):
            if idString[i] != line[i]:
                differenceCount += 1
            else:
                tentativeString += idString[i]  # save the common letters
        if differenceCount == 1:
            answer = tentativeString
print(answer)

import sys

rawInput = sys.stdin.readlines()
input = []
for line in rawInput:
    input.append(line.strip())

fabric = {}


def handleClaim(x, y, w, h):
    for xCoord in range(x, x + w):
        for yCoord in range(y, y + h):
            handleSquare(xCoord, yCoord)
# handle individual points on the fabric


def handleSquare(x, y):
    dictKey = str(x) + "," + str(y)
    if dictKey in fabric:
        fabric[dictKey] += 1
    else:
        fabric[dictKey] = 1


# format of input lines: #123 @ 3,2: 5x4
# this function serves to roughly and quickly get the desired info from the input
def parseInputLine(line):
    pieces = line.split(" ")
    # index 2 and 3 contain the coords/dimensions
    coords = pieces[2].strip(":").split(",")
    dims = pieces[3].split("x")
    vals = int(coords[0]), int(coords[1]), int(dims[0]), int(dims[1])

    return vals


for line in input:
    handleClaim(*parseInputLine(line))


overlapCount = 0
totalCount = 0
for k, v in fabric.items():
    if v > 1:
        overlapCount += 1

print(overlapCount)

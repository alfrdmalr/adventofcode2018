import sys

rawInput = sys.stdin.readlines()
input = []
for line in rawInput:
    input.append(line.strip())

fabric = {}
claims = {}  # key: claim number; value:list of squares associated with that claim


def handleClaim(claimNumber, x, y, w, h):
    claims[claimNumber] = []
    for xCoord in range(x, x + w):
        for yCoord in range(y, y + h):
            handleSquare(claimNumber, xCoord, yCoord)
# handle individual points on the fabric


def handleSquare(claimNumber, x, y):
    dictKey = str(x) + "," + str(y)
    claims[claimNumber].append(dictKey)
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
    vals = pieces[0], int(coords[0]), int(
        coords[1]), int(dims[0]), int(dims[1])

    return vals


for line in input:
    handleClaim(*parseInputLine(line))


for claim, squares in claims.items():
    overlap = False
    for square in squares:
        if fabric[square] > 1:
            overlap = True
            break
    if not overlap:
        print(claim)

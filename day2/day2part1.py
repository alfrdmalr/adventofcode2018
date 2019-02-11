import sys

input = sys.stdin


twoCount = 0
threeCount = 0

for line in input:
	dict = {}
	seenTwo =  False
	seenThree = False

	for letter in line:
		if letter in dict:
			dict[letter] += 1
		else: 
			dict[letter] = 1

	for item, count in dict.items():
		if (count == 3) and not seenThree:
			threeCount += 1
			seenThree = True
		elif count == 2 and not seenTwo:
			twoCount += 1
			seenTwo = True
print twoCount * threeCount
import sys

input = sys.stdin.readlines()

frequency = 0
foundRepeat = False

d = {frequency: 1}

while foundRepeat == False:
	for line in input:
		frequency = frequency + int(line)
		if frequency in d:
			foundRepeat = True
			break
		else: 
			d[frequency] = 1

print frequency
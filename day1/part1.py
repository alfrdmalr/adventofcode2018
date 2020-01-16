import sys

input = sys.stdin

frequency = 0

for line in input:
    frequency = frequency + int(line)

print(frequency)

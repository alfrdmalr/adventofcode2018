import sys
import re

#read from input file and store in a list
rawInput = sys.stdin.readlines()
input = []
for line in rawInput:
    input.append(line.strip())

def chronosort(line):
  # chars 1-17 have date info
  rawDate = line[1:17]
  # remove any delimiters; don't care about them for sorting
  dateNum = "".join(re.split(r'[- :]', rawDate))
  return dateNum

sorted = sorted(input, key = chronosort)

currentGuard = -1
bedtime = -1

# structure: {
#   key: guard number, 
#   value: {key: min, value: #times asleep during this min}
# }
sleepLog = {}
# key: guard no. val: total minutes spent asleep
guardTotals = {}

for line in sorted:
  min = int(line[15:17])
  type = line[19:24] # falls, wakes, or guard; just so happens that they're all 5 chars long
  if type == 'Guard':
    n = re.search(r'#(\d*)', line)
    currentGuard = int(n.group(1)) #use the captured group
    if currentGuard not in guardTotals:
      guardTotals[currentGuard] = 0
  elif type == 'falls':
    bedtime = min
  elif type == 'wakes':
    if currentGuard not in sleepLog:
      sleepLog[currentGuard] = {}
    
    for i in range(bedtime, min):
      # for each minute they're asleep, update the guard's total sleep
      guardTotals[currentGuard] = guardTotals[currentGuard] + 1
      # and update the amount of time they've spent asleep for that exact minute
      if i not in sleepLog[currentGuard]:
        sleepLog[currentGuard][i] = 0
      sleepLog[currentGuard][i] = sleepLog[currentGuard][i] + 1

# find guard who sleeps the most
sleepy = max(guardTotals, key=guardTotals.get)
# find minute they spend asleep the most
favMin = max(sleepLog[sleepy], key=sleepLog[sleepy].get)

print(sleepy * favMin)
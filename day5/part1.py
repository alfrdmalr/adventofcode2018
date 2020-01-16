import sys
import re

#read from input file and store in a list
rawInput = sys.stdin.read()

polymer = rawInput.strip() #goddamnit i forgot to strip the newline
spontaneous = True

def react(pol):
  newPol = ""
  prevChar = ""
  reacted = False

  for i in range(0, len(pol)):
    c = pol[i]
    if prevChar == "":
      prevChar = c
    else: #c is uppercase
      if prevChar.swapcase() == c:
        # print('upper and match')
        prevChar = ""
        reacted = True
      else:
        # print('upper and nonmatch')
        newPol += prevChar
        prevChar = c
  newPol += prevChar

  global polymer
  global spontaneous
  polymer = newPol
  spontaneous = reacted

while spontaneous:
  react(polymer)

print(len(polymer))

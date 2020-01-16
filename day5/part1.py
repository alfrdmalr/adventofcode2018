import sys
import re

#read from input file and store in a list
rawInput = sys.stdin.read()

polymer = rawInput.strip() #goddamnit i forgot to strip the newline

def react(poly):
  pol = poly
  spontaneous = True

  while spontaneous:
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
    pol = newPol
    spontaneous = reacted

  return len(pol)

print(react(polymer))

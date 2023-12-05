import sys
sys.path.append('../lib')
from lib import lineParser
import re
                                         
allLinesParsed = lineParser('./gearRatios.txt', True)

notSpecial = ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

twoDimensionalLines = []
for item in allLinesParsed:
    oneDimensionalArray = []
    oneDimensionalArray.append(item)
    twoDimensionalLines.append(oneDimensionalArray)



for count, line in enumerate(twoDimensionalLines):
    #set current line in list
    currentLine = twoDimensionalLines[count]
    #set next line in list accounting for index range
    if count + 1 < len(twoDimensionalLines):
        nextLine = twoDimensionalLines[count + 1]
    
    for count, character in enumerate(currentLine[0]):
        if character not in notSpecial:
            print(character)
         
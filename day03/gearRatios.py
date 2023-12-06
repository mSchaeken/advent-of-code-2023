import sys
sys.path.append('../lib')
from lib import lineParser
import re
                                         
allLinesParsed = lineParser('./gearRatios.txt', True)

notSpecial = ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
partNumberSum = 0

twoDimensionalLines = []
for item in allLinesParsed:
    oneDimensionalArray = []
    oneDimensionalArray.append(item)
    twoDimensionalLines.append(oneDimensionalArray)



for count, line in enumerate(twoDimensionalLines):
    #set current line in list
    currentLine = twoDimensionalLines[count][0]
    #set next line in list accounting for index range
    if count + 1 < len(twoDimensionalLines):
        nextLine = twoDimensionalLines[count + 1]
    
    #loop through the item (string) in current line and look for special characters
    for count, character in enumerate(currentLine):
        if character not in notSpecial:
            #Initialise empty string and loop through characters
            i = 1
            numString = ''
            while currentLine[count + i].isdigit() and (count + 1) + i < len(currentLine):
                numString += currentLine[count + i]
                i += 1
                if currentLine[count + i].isdigit() == False:
                    partNumberSum += int(numString)
                    break

            j = 1
            numString = ''
            while currentLine[count - j].isdigit() and (count - 1) - j < len(currentLine):
                numString += currentLine[count - j]
                j += 1
                if currentLine[count - j].isdigit() == False:
                    partNumberSum += int(numString)
                    break

print(partNumberSum)
            
            

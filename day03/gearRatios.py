import sys
sys.path.append('../lib')
from lib import lineParser
import re
                                         
allLinesParsed = lineParser('./gearRatios.txt', True)
notSpecial = ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
partNumberSum = 0

#function to look through an item in a list and split the item on digits
def digitFinder(list):
    digits = re.compile(r'(\d+)')
    return digits.split(list[0])

twoDimensionalLines = []
for item in allLinesParsed:
    oneDimensionalArray = []
    oneDimensionalArray.append(item)
    twoDimensionalLines.append(oneDimensionalArray)

#twoDimensionalLines = [[....], [], []]

#loop through entire 2d list
for count, line in enumerate(twoDimensionalLines):
    #set current line in list
    currentLine = twoDimensionalLines[count]
    #set next line in list accounting for index range
    if count + 1 < len(twoDimensionalLines):
        nextLine = twoDimensionalLines[count + 1]
    
    #split current line on digits and look through items until a whole numbers is found
    #then check if adjacent characters are special symbols
    currentLineSplitOnDigits = digitFinder(currentLine)
    for count, item in enumerate(currentLineSplitOnDigits):
        if (count + 1) in range(len(currentLineSplitOnDigits)):
            print(str(currentLineSplitOnDigits[count+1]))
        if item.isdigit() and currentLineSplitOnDigits[count + 1] not in notSpecial:
            partNumberSum += int(item)
        if item.isdigit() and currentLineSplitOnDigits[count - 1] not in notSpecial:
            partNumberSum += int(item)

#print(partNumberSum)

# testString = ['01234567']
# print(testString[0][0])
import sys
sys.path.append('../lib')
from lib import lineParser

#create new list with each line in file as separate item
inputAsList = lineParser('./trebuchet.txt')

#Don't judge me
def wordsToDigit(string):
    return string.lower()\
    .replace('one', 'o1e')\
    .replace('two', 't2o')\
    .replace('three', 't3e')\
    .replace('four', 'f4r')\
    .replace('five', 'f5e')\
    .replace('six', 's6x')\
    .replace('seven', 's7n')\
    .replace('eight', 'e8t')\
    .replace('nine', 'n9e')\

totalSum = 0
#loop through each line in list
for line in inputAsList:
    formattedLine = wordsToDigit(line)
    digitsPerLine = []
    #append each digit in line to array
    for character in formattedLine:
        if character.isdigit() == True:
            digitsPerLine.append(character)
    #cast first and last index of array joined together as int (also accounts for lines with just a single digit)
    digitsAsInt = int(digitsPerLine[0] + digitsPerLine[-1])
    totalSum += digitsAsInt

print('Total sum is ' + str(totalSum))







    
        
        


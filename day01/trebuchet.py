import sys
sys.path.append('../lib')
from lib import lineParser

#create new list with each line in file as separate item
inputAsList = lineParser('./trebuchetThier.txt')

totalSum = 0
#loop through each line in list
for line in inputAsList:
    digitsPerLine = []
    #append each digit in line to array
    for character in line:
        if character.isdigit() == True:
            digitsPerLine.append(character)
    #cast first and last index of array joined together as int (also accounts for lines with just a single digit)
    digitsAsInt = int(digitsPerLine[0] + digitsPerLine[-1])
    totalSum += digitsAsInt

print(totalSum)







    
        
        


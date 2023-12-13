import sys
sys.path.append('../lib')
from lib import lineParser
import re

#testLine = ['Card  27: 54 11 56 55 83 78 47 57 50 19 | 45 70 77 49 12 41 69 78 91 20 51 67  3  6 22 62 27 60  4 63 59 75 43 95 31']                          
allLinesParsed = lineParser('./scratchcards.txt', True)
totalPoints = 0

for line in allLinesParsed:
    #set new variables for winningNums and the amount they match per looped line (card)
    winningNums = []
    amountOfWinningsNumsPerCard = 0

    #loop through winning numbers and append to list
    for item in line.split('|')[0].split(':')[1].split(' '):
        if item.isdigit():
            winningNums.append(item)
    
    #loop through numbers on card and see if they're in winning numbers
    for item in line.split('|')[1].split(' '):
        if item in winningNums:
            amountOfWinningsNumsPerCard += 1
    
    #take amount of winning numbers per line (card) and double 1 that many times
    if amountOfWinningsNumsPerCard == 1:
        totalPoints += 1 
    elif amountOfWinningsNumsPerCard > 1:
        totalPoints += (2 ** (amountOfWinningsNumsPerCard - 1))

print(totalPoints)


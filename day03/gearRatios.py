import sys
sys.path.append('../lib')
from lib import lineParser

def numberJoiner(list):
    numbersJoined = []
    for item in list:
        #set empty string to concatenate digits and counter (index)
        numberString = ''
        i = 0
        #loop through all characters in item and check for digits -> add all digits to list
        for character in item:
            #if character is a digit add it to the number string
            if character.isdigit():
                numberString += str(character)
                #if next character is not a number reset numberString to empty and add current string to list
                if i + 1 < len(item) and item[i + 1].isdigit() == False:
                    numbersJoined.append(int(numberString))
                    numberString = ''
            i += 1
        numbersJoined.append(int(numberString))
    return numbersJoined

#testList = ['100.....15......21.....145....2']

print(numberJoiner(testList))
#parse every line
allLinesParsed = lineParser('./gearRatios.txt', True)
#parse every character in line and save list with index of character and whether they are a number, special symbol or dot
#loop through list, ignoring any dots, until special symbol is reached
#then see if indexes to left and right of special symbol are a number
#if true -> save that number
#then loop through item containing entire line beneath the special symbol and see if any adjacent indexes (so same index, index-1 and index+1) are a number
#if true -> save that number

import sys
sys.path.append('../lib')
from lib import lineParser

maxCountPerGame = {
    'red': 12,
    'green': 13,
    'blue': 14
}

#parse input
allGames = lineParser('./cubeConundrum.txt')

#format each line into comma separated items and append to grabsPerGame
grabsPerGame = []
for grab in allGames:
    grabsPerGame.append(grab.replace(';', ',')\
                        .replace('\n', '')\
                        .replace(':', ','))                  

#split on comma and 
gamesSplitOnComma = []
for grabs in grabsPerGame:
        gamesSplitOnComma.append(grabs.split(','))

id = 0
sumOfIds = 0
#loop through each game and then through each items (grabs) in those games
for game in gamesSplitOnComma:   
    gamePossible = True
    power = 0

    for item in game:
        #ignore gameIds
        if 'Game' in item:
            id += 1        
            continue
        #if number with red higher than maxCount -> game impossible so break
        if 'red' in item and int(item.strip('red ')) > maxCountPerGame['red']:        
            gamePossible = False
            break
        #if number with green higher than maxCount -> game impossible so break
        if 'green' in item and int(item.strip('green ')) > maxCountPerGame['green']:           
            gamePossible = False
            break
        #if number with blue higher than maxCount -> game impossible so break
        if 'blue' in item and int(item.strip('blue ')) > maxCountPerGame['blue']:            
            gamePossible = False
            break
    #if loop didn't break game is possible -> add gameId to sum
    if gamePossible == True:
        sumOfIds += id

#power calculator
sumOfPower = 0
#loop through all games and retain highest grabbed cube count of each  color
for game in gamesSplitOnComma:        
    highestRedCount = 0
    highestGreenCount = 0
    highestBlueCount = 0
    #ignore gameIds
    for item in game:
        if 'Game' in item:
            continue
        if 'red' in item and int(item.strip('red ')) > highestRedCount:
            highestRedCount = int(item.strip('red '))
        if 'green' in item and int(item.strip('green ')) > highestGreenCount:
            highestGreenCount = int(item.strip('green '))
        if 'blue' in item and int(item.strip('blue ')) > highestBlueCount:
            highestBlueCount = int(item.strip('blue '))
        power = highestRedCount * highestGreenCount * highestBlueCount
    sumOfPower += power

print(sumOfIds)
print(sumOfPower)
    
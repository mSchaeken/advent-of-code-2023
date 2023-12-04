import sys
sys.path.append('../lib')
from lib import lineParser

maxCountPerGame = {
    'red': 12,
    'green': 13,
    'blue': 14
}

allGames = lineParser('./cubeConundrum.txt')
grabsPerGame = []
#format each line into comma separated items
for grab in allGames:
    grabsPerGame.append(grab.replace(';', ',')\
                        .replace('\n', '')\
                        .replace(':', ','))                  
#print(grabsPerGame)
                    
#split on comma
gamesSplitOnComma = []
for grabs in grabsPerGame:
        gamesSplitOnComma.append(grabs.split(','))
print(gamesSplitOnComma)

sumOfIds = 0
id = 0
for game in gamesSplitOnComma:   
    gamePossible = True
    for item in game:
        if 'Game' in item:
            id += 1        
            continue
        #if number with red higher than maxCount -> game impossible so break
        if 'red' in item and int(item.strip('red ')) > maxCountPerGame['red']:            
            #print('break on red')
            gamePossible = False
            break
        #if number with green higher than maxCount -> game impossible so break
        if 'green' in item and int(item.strip('green ')) > maxCountPerGame['green']:           
            #print('break on green')
            gamePossible = False
            break
        #if number with blue higher than maxCount -> game impossible so break
        if 'blue' in item and int(item.strip('blue ')) > maxCountPerGame['blue']:            
            #print('break on blue')
            gamePossible = False
            break
    if gamePossible == True:
         sumOfIds += id
print(sumOfIds)
    
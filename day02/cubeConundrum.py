import sys
sys.path.append('../lib')
from lib import lineParser

allGames = lineParser('./cubeConundrum.txt')
#create empty list b
grabsPerGame = []
#for character in item from list a:
for grab in allGames:
    #split on semicoloms in each item and add to list b
    grabsPerGame.append(grab.split(';'))

print(grabsPerGame)
#   append new separated items to empty list b
#   for character in item from list b:
#       create empty list c
#       split on commas
#       append to list c

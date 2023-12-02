import os
import math

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

text =  open_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
textConfig = {
    'red': 12,
    'green':13,
    'blue' : 14,
}
arrFromText = text.split('\n')


test = open_file(os.path.join(os.path.dirname(__file__), 'test.txt'))
testConfig = {
    'red': 12,
    'green':13,
    'blue' : 14,
}
arrFromTest = test.split('\n')
testOutput = 8

#struct
# [gameId : [{red:, green, blue}, ...]]
cubes = ['red', 'green', 'blue']
def formatGame(item):
    game = item.split(':')
    gameId = game[0].strip().split(' ')[1]
    rounds = game[1].split(';')
    gameOp = []
    for round in range(len(rounds)):
        roundCubes = rounds[round].split(',')
        roundConfig = {}
        for k in range(len(roundCubes)):
            cube = roundCubes[k]
            cubeConfig = {}
            cubeSet = cube.strip().split(' ')
            
            cubeConfig[cubeSet[1]] = cubeSet[0]
            roundConfig[cubeSet[1]] = cubeSet[0]
        gameOp.append(roundConfig)
    return gameId, gameOp


def getSumPossibleGameIds(matches):
    possibleGameIdSum = 0
    for i in range(len(matches)):
        matchId, games = formatGame(matches[i])
        possibleMatch = True
        for k in range(len(games)):
            config = textConfig.copy()
            round = games[k]
            for cube in round.keys():
                
                config[cube] = config[cube] - int(round[cube])
            if config['red'] < 0 or config['green'] < 0 or config['blue'] < 0:
                possibleMatch = False
        if possibleMatch:
            possibleGameIdSum += int(matchId)
    return possibleGameIdSum


print(getSumPossibleGameIds(arrFromText))



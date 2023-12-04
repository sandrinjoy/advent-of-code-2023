import os
import math

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

text =  open_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
test = open_file(os.path.join(os.path.dirname(__file__), 'test.txt'))

def formatInput(line):
    
    #struct {gameId: {
    # winning:[]
    # numbers:[]
    # }}
    game = line.split(':')
    gameId = game[0].strip()
    id = gameId.split(' ')[1]
    data =  game[1].strip().split('|')
    winning = list(filter(None,data[0].strip().split(' ')))   
    numbers = list(filter(None,data[1].strip().split(' ')))
    return id, winning, numbers

def totalPointsWinning(text):
    total = 0
    textArr = text.split('\n')
    for i in range(len(textArr)):
        gameId, winning, numbers = formatInput(textArr[i]) 
        points = 0
        for j in range(len(winning)):
            if winning[j] in numbers:
                if points == 0:
                    points = 1
                else:
                    points *= 2
        print(gameId, points)
        total += points
    return total
       



print(totalPointsWinning(text))
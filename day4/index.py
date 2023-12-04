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
    
    id = gameId.strip().split('Card')[1].strip()
    
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
        
        total += points
    return total

def makeMem(text):
    mem = {}
    textArr = text.split('\n')
    for i in range(len(textArr)):

        gameId, winning, numbers = formatInput(textArr[i]) 
        
        mem[int(gameId)] = {
            'winning': winning,
            'numbers': numbers
        }
    return mem
def totalScratchCards(text):
    total = 0
    # this will contain the count of card copies received
    mem = {}
    dataMem = makeMem(text)
    

    textArr = text.split('\n')
    for i in range(len(textArr)):
        gameId, winning, numbers = formatInput(textArr[i]) 
        copiesWon = 0
        for j in range(len(winning)):
            if winning[j] in numbers:
                copiesWon += 1
        for k in range(copiesWon):
            copyId =int(gameId)+ k+1
            if copyId in mem.keys():
                mem[copyId] += 1
            else:
                mem[copyId] = 1
       
        # now do for the copies of the same card
        if int(gameId) in mem.keys():
            memCopies = mem[int(gameId)]
            for i in range(memCopies):
                winning = dataMem[int(gameId)]['winning']
                numbers = dataMem[int(gameId)]['numbers'] 
                copiesWon = 0
                for j in range(len(winning)):
                    if winning[j] in numbers:
                        copiesWon += 1
                for k in range(copiesWon):
                    copyId =int(gameId)+ k+1
                    if copyId in mem.keys():
                        mem[copyId] += 1
                    else:
                        mem[copyId] = 1


    for key in dataMem.keys():
        if key not in mem.keys():
            mem[int(key)] = 1
        else:
            mem[int(key)] += 1
    for key in mem.keys():
        total += mem[int(key)]
    print(total, mem)

            
    return total
        
        



print(totalPointsWinning(text))
print(totalScratchCards(text))
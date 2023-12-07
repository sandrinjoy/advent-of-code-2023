import sys
import math
from collections import defaultdict

kindWeights = {
    'Five': 7,
    'Four': 6,
    'FullHouse': 5,
    'Three': 4,
    'TwoPair': 3,
    'Pair': 1,
    'High': 0
}
cardWeights = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
}

cardWeights2 = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'T': 11,
    '9': 10,
    '8': 9,
    '7': 8,
    '6': 7,
    '5': 6,
    '4': 5,
    '3': 4,
    '2': 3,
    'J': 2,
}

# part 1
with open(sys.argv[1], 'r') as my_file:
    F = my_file.read().strip().split('\n')
    prevWeight = 0 
    handDict = []
    for l in F:
        hand, bid= l.split()
        handArr = list(hand)
        currentHand = handArr

        # create hand obj
        handWeights = defaultdict(int)
        posScore = 0
        for i, c in enumerate(currentHand):
            handWeights[c] += 1
            posScore = posScore * (5*14-i) + cardWeights[c] 

        kindScore = 0
        for k, v in handWeights.items():
            if v == 5:
                kindScore += kindWeights['Five']
            elif v == 4:
                kindScore += kindWeights['Four']
            elif v == 3:
                kindScore += kindWeights['Three']
            elif v == 2:
                kindScore += kindWeights['Pair']
        handDict.append({'bid':int(bid),'kindScore': kindScore, 'posScore': posScore, 'hand': hand})
    arr = sorted(handDict, key=lambda x: (x['kindScore'], x['posScore']))
    sum = 0 
    for i, h in enumerate(arr):
        sum += (i+1) * h['bid']
    print("p1 => ", sum)


# part 2 
with open(sys.argv[1], 'r') as my_file:
    F = my_file.read().strip().split('\n')
    prevWeight = 0 
    handDict = []
    for l in F:
        hand, bid= l.split()
        handArr = list(hand)
        currentHand = handArr

        # create hand obj
        handWeights = defaultdict(int)
        posScore = 0
        for i, c in enumerate(currentHand):
            handWeights[c] += 1
            posScore = posScore * (5*14-i) + cardWeights2[c] 

        jokers = handWeights['J']
        if jokers > 0 and jokers < 5:
            del handWeights['J']
            sortedCards = sorted(handWeights, 
                key=lambda x: (handWeights[x], cardWeights2[x]))[-1]
            handWeights[sortedCards] += jokers
        kindScore = 0
        for k, v in handWeights.items():
            if v == 5:
                kindScore += kindWeights['Five']
            elif v == 4:
                kindScore += kindWeights['Four']
            elif v == 3:
                kindScore += kindWeights['Three']
            elif v == 2:
                kindScore += kindWeights['Pair']
        handDict.append({'bid':int(bid),'kindScore': kindScore, 'posScore': posScore, 'hand': hand})
    arr = sorted(handDict, key=lambda x: (x['kindScore'], x['posScore']))
    sum = 0 
    for i, h in enumerate(arr):
        sum += (i+1) * h['bid']
    print("p2 => ", sum)
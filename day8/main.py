import sys
import math
from collections import defaultdict

RIGHT = 'R'
LEFT = 'L'
# part 1
with open(sys.argv[1], 'r') as my_file:
    F = my_file.read().strip().split('\n')
    steps  = 0
    directions = list(F[0])
    F.pop(0)
    F.pop(0)
    dic = defaultdict(str)
    loc = "AAA"
    dest ="ZZZ"
    for i, v in enumerate(F):
        key, value = F[i].strip().split(' = ')
        l, r = value.strip().strip('(').strip(')').split(', ')
        dic[key+LEFT] = l
        dic[key+RIGHT] = r
    while loc != dest:
        if directions[0] == 'L':
            loc = dic[loc+LEFT]
            directions.pop(0)
            directions.append('L')
        else:
            loc = dic[loc+RIGHT]
            directions.pop(0)
            directions.append('R')
        steps += 1
        

    print("p1 => ", steps)
import sys
import math
with open(sys.argv[1], 'r') as my_file:
    F = my_file.read().strip().split('\n')
    time= F[0].split(':')[1:][0].strip().split()
    distance = F[1].split(':')[1:][0].strip().split()
    waysList = []
    for i, t in enumerate(time):
        minD = int(distance[i])
        T = int(t)
        waysList.append(0)
        for hold in range(T):
            if hold == 0:
                continue
            remT = T - hold
            remD = remT * hold
            maxD =  remD
            if remD > minD:
                waysList[i] += 1
    print("p1 =>", math.prod(waysList))

    T= int(F[0].split(':')[1:][0].replace(" ", ""))
    minD = int(F[1].split(':')[1:][0].replace(" ", ""))
    ways = 0
    for hold in range(T):
        if hold == 0:
            continue
        remT = T - hold
        remD = remT * hold
        maxD =  remD
        if remD > minD:
            ways += 1
    print("p2 =>", ways)
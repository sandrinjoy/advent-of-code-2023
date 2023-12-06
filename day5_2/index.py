import os

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

text =  open_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
test = open_file(os.path.join(os.path.dirname(__file__), 'test.txt'))

def getIntersection(aStart, aRange, bStart, bRange):
    aEnd = aStart + aRange
    bEnd = bStart + bRange
    
    intersectionStart = max(aStart, bStart)
    intersectionEnd =  min(aEnd, bEnd)
    intersectionLength =    intersectionEnd - intersectionStart
    return intersectionStart, intersectionLength

def formatInput(text):
    elements = []
    textArr = text.split('\n')
    seeds = textArr.pop(0).split(':')[1].strip().split()
    for i in range(7):
        elements.append([])
        textArr.pop(0)
        textArr.pop(0)
        while  len(textArr) > 0 and textArr[0] != '':
            
            elements[i].append(textArr[0].strip().split())
            textArr.pop(0)
    return seeds, elements


def getLocationNumbers(text):
    seeds, maps =  formatInput(text)
    
    locations= [ [] for i in range(len(seeds))]
    for i in range(len(seeds)//2):
        pos = i*2+1
        seedRangeGiven = int(seeds[pos])
        seedStart = int(seeds[pos-1])
        bestSeed =  None
        #this will find best seed
        for j in range(len(maps[0])):
            destStart = int(maps[0][j][0])
            sourceStart = int(maps[0][j][1])
            rangeGiven = int(maps[0][j][2])
            for k in range(rangeGiven):
                for l in range(seedRangeGiven):
                    if (seedStart+l) == (sourceStart+k):
                        bestSeed = destStart + k
                        break
        print(bestSeed)
        locations[i].append(bestSeed)
        # maps 
        # dest start, source start, range
        # 12, 50, 4
        # 12 -> 50, 13 -> 51, 14 -> 52, 15 -> 53

        # destStart will be the mapFrom we consider to check
        for j in range(len(maps)): 
            mapFrom = locations[i][-1]
            for k in range(len(maps[j])):
                destStart = int(maps[j][k][0])
                sourceStart = int(maps[j][k][1])
                rangeGiven = int(maps[j][k][2])
                # print(mapFrom, sourceStart, destStart,rangeGiven)
                if (mapFrom >=sourceStart) and (mapFrom < (sourceStart+rangeGiven)):
                    locations[i].pop()
                    locations[i].append(destStart + (mapFrom - sourceStart))
                    break
                if k == len(maps[j])-1:
                    locations[i].pop()
                    locations[i].append(mapFrom)
                    continue
            
    
    return locations

def getLowestLocationNumber(locations):
    print(locations)
    seedLocations = []
    for i in range(len(locations)):
        if len(locations[i]) > 0:
            seedLocations.append(locations[i][-1])
    return min(seedLocations)

#What is the lowest location number that corresponds to any of the initial seed numbers?
print(getLowestLocationNumber(getLocationNumbers(text)))
import random

def slope(point1, point2):
    run = point2[1] - point1[1]
    rise = point2[0] - point1[0]
    #print(f"{rise} / {run}")
    m = rise / run
    return m

def findB(point1,point2):
    m = slope(point1, point2)
    b = (-1 * (m * point1[1])) + point1[1]
    return b

def solveY(x, point1, point2):
    m = slope(point1, point2)
    b = findB(point1, point2)
    y = (m * x) + b
    return y

def fPer(avgLit):
    num = avgLit + 1
    calcList = []
    for x in range(int(round(num))):
        y = solveY(x, [0,0], [50 / (avgLit * 2),num / 2])
        #essentially we take a bar graph with equal bars to the 50 / avgLit * 2 that represents the pairs of litsizes with equal percetnages
        #we then rotate the graph so 0,0 is on the graph around the avg of all possible lit sizes and that number we found before
        #we now have a bunch of different percentages but beacuse it is still the same line with the same bars everything was changed proptionally
        #therfore still equalling 50 in total
        #print(f"{x}: {y}")
        calcList.append(y)
#        counter = 0
    # for x in calcList:
    #     print(x)
    #     counter += x * 2
    return calcList

def makePairs(avgLit):
    maxRange = avgLit * 2
    pairList = []
    counter = 0
    for x in range(int(round(maxRange))):
        if counter == maxRange - counter:
            pairList.append(["apex", avgLit])
            break
        pairList.append([counter, maxRange - counter])
        counter += 1
    return pairList

def percPair(avgLit):
    avgLit = int(round(avgLit))
    percentages = fPer(avgLit)
    pairs = makePairs(avgLit)
    percentPairs = {}
    counter = 0
    for x in range(int(round(avgLit))):
        percentPairs[x] = percentages[x + 1]
    percentPairs[avgLit] = 50
    for x in pairs:
        if x[0] == "apex":
            pass
        else:
            try:
                percentPairs[x[1]] = percentPairs[x[0]]
            except:
                a = 0
                #print(f"percentPairs = {percentPairs}")
    return percentPairs

def chanceCalc(avgLit):
    percentagePairs = percPair(avgLit)
    #print(f"perpairs = {percentagePairs}")
    chance = {}
    connectingDict = {}
    runningTotal = 0
   # print(f"num is {int(round(((avgLit * 2) + 1)))}")
    #print(f"num is int(round(({(avgLit * 2)} + 1)))")
    for x in range(int((((round(avgLit) * 2) + 1)))):
        #print(x)
        prevTotal = runningTotal
        #print(f"percentageParis are : {percentagePairs}")
        try:
            runningTotal += percentagePairs[x]
        except:
            print(f"avgLit is {avgLit}, x is {x}, percentagePairs is {percentagePairs}, prevTotal is {prevTotal}, running total is {runningTotal}, rounded is {round(avgLit)}")
        connectingDict[runningTotal] = prevTotal
        chance [runningTotal] = x
    #print(connectingDict)
    #print(chance)
    return [chance, connectingDict]

def litterCounter(avgLit):
    dicts = chanceCalc(avgLit)
    chance = dicts[0]
    connect = dicts[1]
    randy = random.randint(0,100)
    #print(randy)
    for x in connect.keys():
        if randy >= connect[x] and randy < x:
            if randy == 100:
                print("100 yeah")
            if randy == 101:
                print("am i right")
            if randy == 0:
                print("0 am i right")
            return chance[x]
    if randy == 100:
        return chance[100]

#print(50/8)
#print(slope([0,0], [(6.25), 2.5]))
#print(findB([0,0], [(50/8), 2.5]))
#litterCounter(4)
calcList = []
# for x in range(5):
#     y = solveY(x, [0,0], [6.25,2.5])
#     #6.25 is 50 / 8 which happens to also be something 50 / (9the starting number - 1 the amount of 50% already) or 50 / (9-1)
#     #2.5 is the average of (9-1) / 2 (this is assuming your data goes from 1-4 so 1 + 4 / 2 is 2.5 which is the middle data point, this method can also include zero but doesnt need to)
#     #these two points become a coordinate that becomes the rotating point for my graph
#     #then i find the equation of the line then can solve y for all the x points along the way coming up with the percetnages of my pairs
#     #you then pair the biggest with the two adjacent to the 50% then work your way down from there


#     print(f"{x}: {y}")
#     calcList.append(y)
#     counter = 0
# for x in calcList:
#     print(x)
#     counter += x * 2

#a = determinePercentages(4)
# a = fPer(4)
# print(f"a is {a}")
# # print(makePairs(5))
# print(f"chance is {chanceCalc(4)}")
# #print(f"litterCounter = {litterCounter(4)}")
# calcList = {}
# for x in range(100):
#     l = litterCounter(4)
#     if l in calcList.keys():
#         calcList[l] += 1
#     else:
#         calcList[l] = 1

# print(calcList)
#





# print(chanceCalc(2))
# for x in range (100, 300):
#     y = x / 100
#     print(y)
#     print(litterCounter((x) / 100))
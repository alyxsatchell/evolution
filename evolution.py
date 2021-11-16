from random import randint, randrange
import math
import time
from threading import Thread
import sys
import os
import matplotlib
import matplotlib.pyplot as plt
from statistics import mean
import json
from mathScript import litterCounter
import statistics
#import grpahics

global pi
pi = 3.14159265359
global chartSize
chartSize = 20
global mapSize
mapSize = 100
thread_running = True
global inputTaken
inputTaken = False
halt = False
global afking
afking = False
global mutationRate
mutationRate = [1,10] #1  out of 100

#genomes [0visionLength, 1 placeHolder, 2speed how far a organ can move in one turn, 3size is the radius of the organsim, 4 breeding threshold, 5 avgerage litter size]

#the class that is the ogransims that evovle
class organsim:
    def __init__(self, name, lifeState, pos, gender, genome, energy, status):
        self.name = name
        self.gender = gender
        self.lifeState = lifeState
        self.pos = pos
        self.genome = genome
        self.energy = energy
        self.status = status
    def __str__(self):
        return ("|" + str(self.name).ljust(chartSize) + "|" + str(self.gender).ljust(chartSize) + "|" + str(self.lifeState).ljust(chartSize) + "|" + str(self.pos).ljust(chartSize) + "|" + str(self.genome).ljust(28) + "|" + str(self.energy).ljust(chartSize) + "|" + str(self.status).ljust(chartSize) + "|")

class plant:
    def __init__(self, name, lifeState, pos, maxEnergy, age, energy):
        self.name = name
        self.lifeState = lifeState
        self.pos = pos
        self.maxEnergy = maxEnergy
        self.age = age
        self.energy = energy
    def __str__(self):
        return ("|" + str(self.name).ljust(chartSize) + "|" + str(self.lifeState).ljust(chartSize) + "|" + str(self.pos).ljust(chartSize) + "|" + str(self.maxEnergy).ljust(chartSize) + "|"+ str(self.age).ljust(chartSize) + "|" + str(self.energy).ljust(chartSize) + "|")

def hello():
    print("Hello World!")

def dumpPos(data):
    with open('pos.json', 'w') as fp:
        json.dump(data, fp)

def loadPos():
    with open('pos.json', 'r') as fp:
        data = json.load(fp)
        return data

#degrees to radians
def dgTR(dg):
    print(dg)
    return dg * pi / 180

#radians to degrees
def rTDg(rad):
    return rad * 180/pi

def dgOF(num):
    num = int(num)
    # if num >= 360:
    ans = num % 360
    return ans

def findA(maxEnergy, root1, root2):
    # y = a(x-h)^2 + k
    #print(f"maxen = {maxEnergy} root1 is {root1} and root2 is {root2}")
    k = maxEnergy
    h = (root2[1] + root1[1]) / 2
    #print(f"k is {h} found through {root2[1]} - {root1[1]}")
    # 0 = a"(x-h)^2" + k
    #print(f"({root1[1]} - {h}) ** 2")
    coefficentofA = (root1[1] - h) ** 2
    #print(f"a is coefficentofA is {coefficentofA}")
    #  a(x-h) ^ 2 = k
    # a = k / (x - h) ^ 2
    a = k * - 1 / coefficentofA
    #a = (0 - k) / (root1[1] - h)
    return a

#y = a(x-h)^2 + k
def findY(flora):
    maxEnergy = flora.maxEnergy
    vertex = (maxEnergy, 3)
    a = findA(maxEnergy, (0,1), (0,5))
    y = (a * ((flora.age - 3) ** 2)) + maxEnergy
    return y

def plantLifeCycle(flora):
    maxEnergy = flora.energy
    a = findA(maxEnergy, (0,1), 0,5)
    currentEnergy = a

#finds to distance between two points
def distance(point1, point2):
    d = float(math.sqrt(float(((float(point1[0]) - float(point2[0])) ** 2) + ((float(point1[1]) - float(point2[1])) ** 2))))
    #print(f"d is {d}")
    return d

#checks if a point is in a circle based on the radius and centre
def pointInCircle(r,point1,point2):
    state = False
    d = distance(point1, point2)
    #print(f"d is {d} and r is {r}")
    if d <= r:
        state = True
    return state

def relative(point1, point2):
    return [point2[0] - point1[0], point2[1] - point1[1]]

def heading (point1, point2):
    rel = relative(point1, point2)
    #print(f"rel is {rel}")
    return math.atan2(rel[1], rel[0])

def inCone(point1, point2, r, rCone):
    # print(f"pic {pointInCircle(r,point1,point2)}")
    if pointInCircle(r, point1, point2):
        # print("In Circle")
        head = heading(point1, point2)
        #print(head)
        if point1 == point2:
            return True
        #print(f"{head} >= {rCone[0]} and {head} <= {rCone[1]} which is {head >= dgTR(rCone[0]) and head <= dgTR(rCone[1])}")
        if head >= dgTR(rCone[0]) and head <= dgTR(rCone[1]):
            #print("in cone")
            return True
            print("lol")
    return False

def inp():
    message = "foo: "
    uin = input(message)
    return uin

def testering():
    #print("Yep it doing stuff")
    counter = 0
    while True:
        counter += 1
        print(counter)
        time.sleep(1.0)

def afk():
    global thread_running
    global halt
    global inputTaken
    if afking == True:
        startTime = time.time()
        while thread_running:
            #print(f"input Taken = {inputTaken}")
            if inputTaken == True:
                startTime = time.time()
                inputTaken = False
            #print(f"lol {(time.time() - startTime)}")
            if (time.time() - startTime) >= 12.0:
                halt = True
                os._exit(1)
                raise("The END!")
                quit()
                sys.exit()

def my_forever_while():
    global thread_running

    start_time = time.time()

    # run this while there is no input
    while thread_running:
        time.sleep(0.1)

        if time.time() - start_time >= 15:
            start_time = time.time()
            print('Another 5 seconds has passed')

def take_input():
    user_input = input('Type user input: ')
    # doing something with the input
    print('The user input is: ', user_input)


#turns a number under 3999 into a roman numeral letters
def numToRomLetter(num):
    mil = math.floor(int(num) / 1000)
    lftMil = int(num) % 1000
    hMil = math.floor(lftMil / 500)
    lftHMil = lftMil % 500
    cent = math.floor(lftHMil / 100)
    lftCent = lftHMil % 100
    hCent = math.floor(lftCent / 50)
    lftHCent = lftCent % 50
    dec = math.floor(lftHCent / 10)
    lftDec = lftHCent % 10
    hDec = math.floor(lftDec / 5)
    lftHDec = lftDec % 5
    mon = lftHDec
    return [mil,hMil, cent, hCent, dec, hDec, mon]

#turns num under 3999 into a full orman numeral number
def numToRom(number):
    romanLetters = numToRomLetter(number)
    num = ""

    # numToLetter = ["I", "V", "X", "L", "C", "D", "M"]
    numToLetter = ["M", "D", "C", "L", "X", "V", "I"]
    breaker = False
    passer = False
    for index,x in enumerate(romanLetters):
        if breaker == True:
            break
        if int(x) > 3:
            if passer == False:
                num+= f"{numToLetter[index] * (5-int(x))}{numToLetter[index - 1]}"

        else:
            passer = False
            if int(x) == 1 and index != 6:
                if romanLetters[index + 1] == 4:
                    num+= f"{numToLetter[index+1]}{numToLetter[index-1]}"
                    passer = True
                    
                else:
                    a = 0
            if passer == False:
                num+= f"{numToLetter[index] * int(x)}"
    return(num)

def romNumAdd(rom,num):
    romNum = romToNum(rom)
    ans = int(romNum) + int(num)
    return [numToRom(ans), ans]

def romToNum(letters):
    num = 0
    numToLetter = ["M", "D", "C", "L", "X", "V", "I"]
    letterToNum = {"M": 1000, "D": 500, "C" : 100, "L" : 50, "X" : 10, "V" : 5, "I" : 1}
    for index, letter in enumerate(letters.upper()):
        try:
            if letterToNum[letters[index+1]] > letterToNum[letter]:
                num -= letterToNum[letter]
            else:
                num+= letterToNum[letter]
        except:
            num += letterToNum[letter]
    return num

def chartHeader(sample):
    finalString = ""
    objectVar = vars(sample)
    for x in objectVar.keys():
        if str(x) == "genome":
            finalString += (f"|{(str(x).ljust(28))}")
        else:
            finalString += (f"|{(str(x).ljust(chartSize))}")
    print(finalString + "|")
    print("_" * len(finalString))
    return finalString

def chartBody(popArray):
    # for x in popArray:
    #     print(x.__str__())
    for x in popArray.values():
        print(x.__str__())

def show(popArray):
    for x in popArray.values():
        xVar = x
        break
    try:
        chartHeader(xVar)
        chartBody(popArray)
    except:
        print(popArray)

def nameChecker(newPop, popArray):
        for named in popArray.keys():
            if named == newPop.name:
                for index, x in enumerate(str(newPop.name)):
                    if x.isalpha():
                        title = newPop.name[index:]
                        newPop.name = newPop.name[:index] + romNumAdd(title,1)[0]
                        break
                if str(newPop.name).isnumeric():
                    newPop.name = str(newPop.name) + "II"

def genPop(popArray, genSize):
    counter = 0
    while True:
        if counter >= genSize:
            break
        if randint(0,1):
            gender = "M"
        else:
            gender = "F"
        newPop = organsim(randrange(0,1), 1, [randrange(-mapSize,mapSize), randrange(-mapSize,mapSize)], gender, [randrange(10,30),1,randrange(10,20),randrange(4,5),randrange(500,1000), 2], randrange(500,999), "")
        # popArray.append(newPop)
        # 25, [0,0], [25,[0,270],25,1,300], 100, ""
        nameChecker(newPop, popArray)
        # for named in popArray.keys():
        #     if named == newPop.name:
        #         for index, x in enumerate(str(newPop.name)):
        #             if x.isalpha():
        #                 title = newPop.name[index:]
        #                 newPop.name = newPop.name[:index] + romNumAdd(title,1)[0]
        #                 break
        #         if str(newPop.name).isnumeric():
        #             newPop.name = str(newPop.name) + "II"

        popArray [newPop.name] = newPop
        counter += 1
    return popArray

def genPlant(popArray, genSize):
    counter = 0
    while True:
        if counter >= genSize:
            break
        newPop = plant(randrange(0,100), 1, [randrange(-mapSize,mapSize), randrange(-mapSize,mapSize)], randrange(300,700), 1, 0)
        # popArray.append(newPop)
        for named in popArray.keys():
            if named == newPop.name:
                for index, x in enumerate(str(newPop.name)):
                    if x.isalpha():
                        title = newPop.name[index:]
                        newPop.name = newPop.name[:index] + romNumAdd(title,1)[0]
                        break
                if str(newPop.name).isnumeric():
                    newPop.name = str(newPop.name) + "II"

        popArray [newPop.name] = newPop
        counter += 1
    return popArray

def move(point1, dist, head):
    x = dist * math.cos(head)
    y = dist * math.sin(head)
    dest = [round(point1[0] + x, 5), round(point1[1] + y, 5)]
    return dest

def moveTo(point1, point2):
    dist = distance(point1, point2)
    head = heading(point1, point2)
    mve = move(point1, dist, head)
    return mve

def energyCost(dist):
    return dist
    #return (dist ** 1.7)

def movementP(organ, point2):
    organ.pos = moveTo(organ.pos, point2)

def moveD(organ, point2):
    #print(organ.genome[2])
    organ.pos = move(organ.pos, organ.genome[2], heading(organ.pos, point2))

def findPlants(point1, plantDict, disMod = 0.7, enMod = 0.3, organ="None"):
    #print(type(plantDict))
    scoreDict = {}
    if type(plantDict) is dict:
        for x in plantDict.values():
            dis = distance(point1,x.pos)
            en = x.energy
            score = (dis * disMod) + (en * enMod)
            if score in scoreDict:
                scoreDict[score].append(x)
            else:
                scoreDict[score] = [x]
        scoreList = []
    elif type(plantDict) is list:
        for x in plantDict:
            if x == organ:
                continue
            else:
                dis = distance(point1,x.pos)
                en = x.energy
                score = (dis * disMod) + (en * enMod)
                if score in scoreDict:
                    scoreDict[score].append(x)
                else:
                    scoreDict[score] = [x]
        scoreList = []
    else:
        #print(f"so the type you gave me is a {type(plantDict)}")
        #print("Ya didnt give me a plantDict no idea what in the world you gave me but it was not a plantDict come back with a plantDict cuz this is not one")
        return False
    #print(f"scoreDict is {scoreDict}")
    for x in scoreDict.keys():
        scoreList.append(x)
        #print(f"scoreList is {scoreList}")
    scoreList.sort()
    #print(f"scoreList {scoreList}")
    try:
        counter = 0
        while True:
            bestScore = scoreList[counter]
            #print(f"best score {bestScore}")
            bestPlant = scoreDict[bestScore] [counter]
            if type(bestPlant) == organsim:
                if bestPlant.lifeState == 1:
                    return bestPlant
                else:
                    counter += 1
            else:
                return bestPlant
    except:
        return None


def findPlantInSight(organ,plantDict,disMod = 0.7, enMod = 0.3, includeSelf = 0):
    possible = []
    #print(f"plantdict values {plantDict.values()}")
    for x in plantDict.values():
        #print(f"x is {x.name} and is {organ.name}")
        if x == organ:
            if includeSelf == 1:
                #print("this do be me")
                continue
                print()
        #print(f"in cone if = {organ.pos, x.pos, organ.genome[0], organ.genome[1]}")
        if inCone(organ.pos, x.pos, organ.genome[0], organ.genome[1]):
            #print("added")
            possible.append(x)
    #print(f"possible is {possible}")
    return possible

def findPlantInCircle(organ, plantDict):
    possible = []
    for x in plantDict.values():
        if x == organ:
            continue
        else:
            if pointInCircle(organ.genome[0], organ.pos, x.pos):
                possible.append(x)
    return possible


def moveP(organ, plantDict, includeSelf = 0):
    #print(type(plantDict))
    bPlant = findPlants(organ.pos,findPlantInCircle(organ, plantDict))
    if bPlant == None:
        return("None")
    # print(f"bplant {bPlant}")
    # print(f"distance stuff thingy {distance(organ.pos, bPlant.pos)} > {organ.genome[2]}")
    d = distance(organ.pos, bPlant.pos)
    if d > organ.genome[2]:
        moveD(organ, bPlant.pos)
        organ.energy -= energyCost(organ.genome[2])
    else:
        movementP(organ, bPlant.pos)
        organ.energy -= energyCost(d)
    return("Fun")

def wander(organ):
    randDirection = randrange(-180, 180)
    #print(f"randDirection is {randDirection}")
    vis = organ.genome[1]
    organ.pos = move(organ.pos, organ.genome[2], dgTR(randDirection))
    organ.energy -= energyCost(organ.genome[2])
    visRange = abs(vis[0] - vis[1]) / 2
    #print(f"visRange is {abs(vis[0] - vis[1]) / 2} = {visRange}")
    organ.genome[1] = [dgOF(randDirection - visRange), dgOF(visRange + randDirection)]

def consume(organ, food, plantDict):
    organ.energy += food.energy * 0.5
    plantDict.pop(food.name)

def eat(organ, plantDict):
    foodList = []
    for potFood in plantDict.values():
        if distance(organ.pos, potFood.pos) <= organ.genome[3]:
            foodList.append(potFood)
    for x in foodList:
        consume(organ, x, plantDict)

def mutate(value):
    #print(f"vlaue is {value} type is {type(value)}")
    randy = randint(mutationRate[0],mutationRate[1])
    #print(f"randy is {randy}")
    if randy <= mutationRate[0]:
        value = round(value * 1.1, 5)
        # print("a mutation has occured")
    return value

def makeGenome(parentA, parentB):
    child = "bruh"
    geneLength = len(parentA.genome)
    randy = randrange(0, geneLength - 1)
    #print(f"randy {randy}")
    aGenome = parentA.genome
    bGenome = parentB.genome
    # print(f"a genome is pretty much like {aGenome} {bGenome[randy:]} + {aGenome[:randy]}")
    oneGenome = aGenome[:randy] + bGenome[randy:]
    twoGenome = bGenome[:randy] + aGenome[randy:]
    return oneGenome, twoGenome

def litter():
    counter = 0
    while True:
        randy = randint(0,1)
        if randy == 0:
            break
        else:
            counter += 1
    return counter

def breed(parentA, parentB, popArray):
    litterSize = litter()
    print(f"litterSize is {litterSize}")
    offSpring = []
    #print(f"litter size is {litterSize}")
    #en = parentA.energy / (litterSize + 1)
    #en = parentA.energy + parentB.energy / ((litterSize + 3))
    print(f"{parentA.energy} + {parentB.energy} / {(litterSize + 2)}")
    en = (parentA.energy + parentB.energy) / (litterSize + 2)
    print(f"en is {en} which came from {parentA.energy} + {parentB.energy}) / ({litterSize + 2}")
    #parentA.energy = parentA.energy / ((litterSize + 1))
    parentA.energy = 0.7 * en
    print(f"parentA.energy be {parentA.energy}")
    #en += parentB.energy / (litterSize + 1)
    parentB.energy = 0.7 * en 
    #parentB.energy = parentB.energy / ((litterSize + 1))
    print(f"total pop energy = {parentA.energy + parentB.energy + (en * litterSize)}")
    newGenome = makeGenome(parentA,parentB)
    #print(f"genomes are {newGenome}")
    for x in range(litterSize):
        child = organsim(randrange(0,100), 1, [parentA.pos[0] + randrange(3,6), parentA.pos[0] + randrange(3,6)], newGenome[randrange(0,2)], en, "")
        nameChecker(child, popArray)
        nRandy = randint(0, len(child.genome) - 1)
        #print(f"nrandy do be {nRandy} with a genome of {child.genome} nrandy should be {child.genome[nRandy]}")
        while True:
            if nRandy == 1:
                #print("it dealt with this like expected")
                nRandy = randint(0, len(child.genome) - 1)
                #print(f"ok this is new nRandy {nRandy}")
            else:
                break
            
        child.genome[nRandy] = round(mutate(child.genome[nRandy]), 3)
        #popArray[child.name] = child
        offSpring.append(child)
    return offSpring

def litterChance(mCLS):
    if mCLS % 2 == 0:
        max = (mCLS * 2) + 1
        print(f"max is {max}")
        a = findA(50, (0,-1), (0, max))
        print(a)
    else:
        max = (mCLS * 2) + 1
        a = findA(50, (0,-1), (0, max))
        print(a)

def fight(organ, popArray):
    for x in popArray.values():
        if x == organ:
            pass
        else:
            if x.lifeState == 0:
                continue
            elif distance(organ.pos, x.pos) <= organ.genome[3]:
                organ.energy += x.energy / 2
                x.lifeState = 0
                x.status = "eaten"

def moveM(organ, mate):
    d = distance(organ.pos, mate.pos)
    if d > organ.genome[0]:
        moveD(organ, mate.pos)
    else:
        movementP(organ, mate.pos)

def recordPosition(popArray, plantDict):
    dataDict = {"organ" : {}, "plant" : {}}
    for organ in popArray.values():
        dataDict["organ"] [organ.name] = organ.pos
    for plants in plantDict.values():
        dataDict["plant"] [plants.name] = plants.pos
    return dataDict

def posUpdate(popArray, plantDict):
    data = recordPosition(popArray, plantDict)
    dumpPos(data)

def smoothposUpdate(popArray, plantDict, fps):
    delay = 1 / fps
    if delay > 24:
        delay = 24
    currentPosDict = loadPos()
    print(f"pos.json looking like {currentPosDict} rn")
    data = recordPosition(popArray,plantDict)
    print(f"data is {data}")
    newData = {}
    for x in currentPosDict["organ"].keys():
        oldPos = currentPosDict["organ"][x]
        newFinalPos = data["organ"] [x]
        print(f"oldPos is {oldPos} new pos is {newFinalPos}")
        difx = newFinalPos[0] - oldPos[0]
        dify = newFinalPos[1] - oldPos[1]
        smoothPos = []
        counter = 1
        for tempVar2 in range(fps):
            print(f"{difx} / {fps} * {counter}")
            newPos = ([(oldPos[0] / fps) * counter, (oldPos[1] / fps) * counter])
            print(f"newPos is {newPos}")
            smoothPos.append(newPos)
            counter += 1
        print(f"tempVar be {oldPos}")
    dumpPos(data)



def timingBelt(hz, total, myFunc, popArray):
    fps = 1 / hz
    counter = 0
    while True:
        if int(round(counter, 14)) == total:
            print("break")
            break
        counter += fps
        print(counter)
        myFunc(popArray)
        time.sleep(fps)

def smthPosUpdate(popArray, plantDict, fps):
    oldPosDict = loadPos()
    for x in oldPosDict ["organ"]:
        pass

def smoothStep(point1, point2, steps):
    difx = point2[0] - point1[0]
    dify = point2[0] - point1[1]
    ans = []
    for x in range(steps):
        print(x)
        op = x + 1
        print(f"({difx} / ({steps} * {op})) + {point1[0]}")
        ans.append([((difx / steps) * op) + point1[0], ((dify / steps) * op) + point1[1]])
    return ans 

def smoothSteper(popArray, plantDict, steps):
    oldPosDict = loadPos()
    print(f"oldPosDict is {oldPosDict}")
    data = recordPosition(popArray,plantDict)
    print(f"data is {data}")
    newData = {"organ" : {}, "plant" : {}}
    for x in oldPosDict["organ"].keys():
        oldPosTar = oldPosDict["organ"][x]
        print(f"oldPosTar[0] is {oldPosTar[0]}")
        if type(oldPosTar[0]) == list:
            oldPos = oldPosTar[len(oldPosTar) - 1]
            newPos = data["organ"] [x]
        else:
            oldPos = oldPosTar
            newPos = data["organ"] [x]
        print(f"oldPois is {oldPos} and newPos is {newPos}")
        ans = smoothStep(oldPos, newPos, steps)
        newData["organ"] [x] = ans
        print(f"ans = {ans}")
    return newData
    print(f"newData is {newData}")

def recordSmoothPosition(popArray, plants):
    data = {"organ" : {}, "plant" : {}}
    for x in popArray:
        data["organ"] [x] = popArray[x]
    for x in plants:
        data["plants"] [x] = plants[x]
    return data

def smoothTimingBelt(newData, plantDict, nameList, steps, updateDelay):
    newPopArray = {}
    counter = 0
    for y in range(len(newData["organ"] [nameList[0]]) - 1):
        for x in nameList:
            newPopArray [x] = newData["organ"] [x] [counter]
        print(newPopArray)
        data = recordSmoothPosition(newPopArray,plantDict)
        print(data)
        dumpPos(data)
        counter += 1
        sleepyTime = updateDelay / (steps * updateDelay)
        print(f"sleepTime is {sleepyTime}")
        time.sleep(updateDelay / (steps * updateDelay))

def smoothPosUpdater(popArray, plantDict, steps, updateDelay):
    startTime = time.time()
    newData = smoothSteper(popArray, plantDict, steps)
    dataList = []
    nameList = []
    for x in newData["organ"]:
        dataList.append(newData["organ"][x])
        nameList.append(x)
    counter = 0
    newPopArray = {}
    for y in range(len(newData["organ"] [nameList[0]]) - 1):
        for x in nameList:
            newPopArray [x] = newData["organ"] [x] [counter]
        print(newPopArray)
        data = recordSmoothPosition(newPopArray,plantDict)
        print(data)
        dumpPos(data)
        counter += 1
        sleepyTime = updateDelay / (steps * updateDelay)
        print(f"sleepTime is {sleepyTime}")
        time.sleep(updateDelay / (steps * updateDelay))
    #posUpdate(newPopArray,plantDict)

def mating(organ, popArray, breedList):
    if organ in breedList:
        pass
    else:
        breedList.append(organ)
    

def doStuff(popArray, plantDict, breedList):
    offSpring = []
    matingList = []
    for organ in popArray.values():
        if organ.energy <= 0:
            organ.status = "Dead"
            organ.lifeState = 0
            if organ in breedList:
                for index, x in enumerate(breedList):
                    if x == organ:
                        breedList.pop(index)
        if organ.lifeState == 0:
            pass
        else:
            return

def mutate(value):
    mod = 0
    if randint(0,1) == 1:
        mod = 1
    else:
        mod = -1
    changed = value + (value * 0.1 * mod)
    return changed

def genomeMutate(genome):
    if randint(0,1) == 1:
        length = len(genome) - 1
        randy = randint(0,length)
        genome[randy] = mutate(genome[randy])
    return genome

def newGenome(parentA, parentB):
    genome = []
    for index, x in enumerate(parentA.genome):
        if randint(0,1) == 1:
            genome.append(parentA.genome[index])
        else:
            genome.append(parentB.genome[index])
    return genome

def reproduce(parentA, parentB, popArray):
    offSpring = []
    if parentA.gender == "F":
        mother = parentA
        father = parentB
    else:
        mother = parentB
        father = parentA
    litterSize = litterCounter(mother.genome[5])
    for x in range(litterSize):
        if randint(0,1) == 1:
            gen = "F"
        else:
            gen = "M"
        genome = newGenome(parentA,parentB)
        childEn = (parentA.energy + parentB.energy) / (litterSize + 2)
        childOffset = randint(-5,5)
        childLocation = [mother.pos[0] + childOffset, mother.pos[1] + childOffset]
        child = organsim(randrange(0,100), 1, childLocation, gen, genome, childEn, "Born")
        child.genome = genomeMutate(child.genome)
        nameChecker(child, popArray)
        offSpring.append(child)
    return offSpring

def intergrateOffspring(offSpring, popArray):
    for x in offSpring:
        popArray[x.name] = x
    return popArray

def getSpeci(popArray):
    for x in popArray.values():
        subject = x
        break
    return subject

def listAvg(nums):
    return sum(nums) / len(nums)
    #testing commits 22

def averageSkill(popArray):
    avg = {}
    genomeAvg = []
    starterList = ["test"]
    subject = getSpeci(popArray)
    gen = subject.genome
    for index, x in enumerate(gen):
        avg[index] = []
    for x in popArray.values():
        for index, y in enumerate(x.genome):
            avg[index].append(y)
    for x in avg.keys():
        #print(x, avg)
        genomeAvg.append(listAvg(avg[x]))
    return genomeAvg

def scoreMate(potMate, popArray):
    #find way to make every attribute roughly equivalent to determine and give it a score based on that so that the mate readiness is not the only real facotr
    average = averageSkill(popArray)
    skill = []
    #print(potMate.genome, average)
    for index, x in enumerate(potMate.genome):
        skill.append(x / average[index])
    return skill

def numberScoreMate(skill):
    score = 0
    if randint(0,1):
        num = 1
    else:
        num = 0
    scoring = [1,1,1,1,num,1]
    for index,x in enumerate(scoring):
        score += x * skill[index]
    return score

def findBestScoredMate(organ, popArray):
    bestScore = [0,0]
    for x in popArray.values():
        if x == organ:
            continue
        else:
            if organ.gender == x.gender:
                continue
            else:
                newScore = numberScoreMate(scoreMate(x, popArray))
                if newScore > bestScore[1]:
                    bestScore = [x, newScore]
    return bestScore[0]

def dictOfScore(mateList, popArray):
    mateDict = {"M" : {}, "F" : {}}
    for x in mateList:
        mateDict[x.gender] [numberScoreMate(scoreMate(x,popArray))] = x
    return mateDict

def sortScore(mateDict):
    scoreListTemp = []
    nMateDict = {}
    print(f"mateDict is {mateDict}")
    for x in mateDict.keys():
        print(f"x is {x}")
        for score in mateDict[x].keys():
            print(f"score is {score}")
            scoreListTemp.append(score)
        scoreListTemp.sort(reverse=1)
        nMateDict[x] = scoreListTemp
        scoreListTemp = []
    return nMateDict

def matchMakerList(sortedMateDict):
    mateList = []
    for index, x in enumerate(sortedMateDict["M"]):
        male = x
        try:
            female = sortedMateDict["F"] [index]
        except:
            break
        mateList.append([male, female])
    return mateList

def matchMaker(mateList, mateDict):
    objMateList = []
    for x in mateList:
        print(f"x is {x[0]}")
        print(mateList)
        print(mateDict["M"])
        print(mateDict["F"])
        male = mateDict["M"] [x[0]]
        female = mateDict["F"] [x[1]]
        objMateList.append([male,female])
    return objMateList
    
    



def rateMateT(organ, popArray):
    for x in popArray.keys():
        score = 0
        

def turn(popArray, plantDict, breedList):
    offSpring = []
    matingList = []
    for organ in popArray.values():
        if organ.energy <= 0:
            organ.status = "Dead"
            organ.lifeState = 0
            if organ in breedList:
                for index, x in enumerate(breedList):
                    if x == organ:
                        breedList.pop(index)
        if organ.lifeState == 0:
            pass
        else:
            for x in matingList:
                if x[0] == organ:
                    organ.status = f"Mating with {x[1]}"
                    continue
            organ.status = "Moving/Eating PLant"
            #print(f"Plant moving")
            if organ.energy >= organ.genome[4]:
                organ.status = "Looking For Mate"
                if organ in breedList:
                    pass
                else:
                    breedList.append(organ)
                bestMate = findPlants(organ.pos, breedList, organ=organ)
                if bestMate == None:
                    wander(organ)
                else:
                    organ.status = f"Moving towards {bestMate.name}"
                    moveM(organ, bestMate)
                    d = distance(organ.pos, bestMate.pos)
                    if pointInCircle(organ.genome[3], organ.pos, bestMate.pos):
                        organ.status = f"Mating with {bestMate.name}"
                        newOffspring = breed(organ, bestMate, popArray)
                        matingList.append([bestMate, organ])
                        for x in newOffspring:
                            offSpring.append(x)
                        if organ in breedList:
                            for index, x in enumerate(breedList):
                                if x == organ:
                                    breedList.pop(index)
            elif organ in breedList and organ.energy <= organ.genome[4]:
                bestMate = findPlants(organ.pos, breedList, organ=organ)
                if bestMate == None:
                    wander(organ)
                else:
                    organ.status = f"Moving towards {bestMate.name}"
                    moveM(organ, bestMate)
                    d = distance(organ.pos, bestMate.pos)
                    if pointInCircle(organ.genome[3], organ.pos, bestMate.pos):
                        organ.status = f"Mating with {bestMate.name}"
                        newOffspring = breed(organ, bestMate, popArray)
                        matingList.append([bestMate, organ])
                        for x in newOffspring:
                            offSpring.append(x)
                        if organ in breedList:
                            for index, x in enumerate(breedList):
                                if x == organ:
                                    breedList.pop(index)
            
            elif moveP(organ, plantDict) == "None":
                #print(f"Fighting")
                organ.status = "Fight"
                if moveP(organ, popArray,includeSelf=1) == "None":
                    organ.status = "Wander"
                   #print( f"Wandering {organ}")
                    #print(f"wandering")
                    wander(organ)
                fight(organ, popArray)
            eat(organ, plantDict)
    # for x in popArrayCopy:
    #     popArray[x] = popArrayCopy[x]
    for child in offSpring:
        popArray[child.name] = child
        wander(child)
    matingList = []
    plantHitList = []
    for flora in plantDict.values():
        #print(f"flora is {flora}")
        y = findY(flora)
        flora.energy = findY(flora)
        #print(f"flora2 is {flora}")
        flora.age += 1
        if flora.energy < 0:
            plantHitList.append(flora.name)
    for flora in plantHitList:
        plantDict.pop(flora)
    genPlant(plantDict, 30)
    #implemebnt a sperate dict for offspring so not too change size during itterations or have a separate copy looking to go through the itterantins then update after
    #also what the crap is going on with nrandy and list index out of range why no children

def execute(popArray):
    global halt
    global inputTaken
    point1 = [0,0]
    point2 = [-1,1]
    while True:
        if halt == True:
            break
        uin = input()
        if uin == "exit":
            break
        elif uin == "rtn":
            uin = input("Input number to be rtn: ")
            print(romToNum(uin))
        elif uin == "ntr":
            uin = input("Input a number to be ntr: ")
            print(numToRom(uin))
        elif uin == "gpt":
            popArray = genPop(popArray,10)
            show(popArray)
        elif uin == "rna":
            rom = input("Input rom ")
            num = input("Input num ")
            print(romNumAdd(rom,num))
        elif uin == "rel":
            print(relative([1,1], [0,0]))
        elif uin == "heading":
            print((heading([2,2], [5,5])))
            print(heading([2,2], [0,0]))
        elif uin == "inc":
            print(inCone(point1,point2, 1.5, [90,180]))
        elif uin == "mv":
            print(move(point1, math.sqrt(2), -2.356194490192345))
        elif uin == "testPlant":
            testPlantThing = plant("Bob", 1, [1,1], 300)
            show({"Bob" : testPlantThing})
        elif uin == "testGenPlant":
            plants = {}
            genPlant(plants,10)
            show(plants)
        elif uin == "bPlant":
            plants = {}
            genPlant(plants,10)
            show(plants)
            print(show({"" : (findPlants([0,0],plants))}))
        elif uin == "insPlant":
            plants = {}
            popArray = {}
            genPlant(plants,10)
            genPop(popArray,1)
            garry = organsim(randrange(0,1), 1, [randrange(0,mapSize), randrange(0,mapSize)], [1,[0,0.8],1,1], 100)
            show(plants)
            print(findPlantInSight(garry, plants))
            #change to just rpint not show
        elif uin == "insbPlant":
            plants = {}
            popArray = {}
            genPlant(plants,10)
            genPop(popArray,1)
            garry = organsim("garry", 1, [0,0], [3,[0,0.8],1,1], 100)
            show(plants)
            pis = findPlantInSight(garry, plants)
            print(show({"" : (findPlants(garry.pos,pis))}))
        elif uin == "movep":
            plants = {}
            plants["jarry"] = plant("jarry", 1, [10,10], 300)
            genPlant(plants, 1)
            garry = organsim("garry", 1, [0,0], [6,[0,90],5,1], 100, "")
            show(plants)
            moveP(garry, plants)
            show({"garry" : garry})
        elif uin == "moved":
            garry = organsim("garry", 1, [0,0], [5,[0,90],5,1], 100)
            moveD(garry, [6,6])
            print(garry)
        elif uin == "wander":
            garry = organsim("garry", 1, [0,0], [5,[0,90],5,1], 100)
            wander(garry)
            print(garry)
        elif uin == "dgof":
            uin = input("LOL INPUT NUM: ")
            print(dgOF(uin))
        elif uin == "graph":
            try:
                print(garry)
                plt.scatter(garry.pos[0],garry.pos[1])
                plt.show()
            except:
                print("no garry :(")
        elif uin == "visu":
            x_coords = []
            y_coords = []
            for organ in popArray.values():
                x_coords.append(organ.pos[0])
                y_coords.append(organ.pos[1])
            plt.scatter(x_coords, y_coords)
            plt.show()
        elif uin == "con":
            garry = organsim("garry", 1, [0,0], [5,[0,90],5,2], 100)
            plants = {}
            plants["jarry"] = plant("jarry", 1, [1,1], 300)
            consume(garry, plants["jarry"], plants)
            print(plants)
            show({"garry" : garry})
        elif uin == "eat":
            garry = organsim("garry", 1, [0,0], [5,[0,90],5,2], 100)
            plants = {}
            plants["jarry"] = plant("jarry", 1, [1,1], 300)
            plants["barry"] = plant("barry", 1, [2,2], 300)
            eat(garry,plants)
            print(plants)
            show({"garry" : garry})
        elif uin == "mutate":
            counter = 0
            counterList = []
            for x in range(100):
                counter = 0
                for x in range(100):
                    mutt = mutate(1)
                    if mutt == 1.1:
                        #print("yep")
                        counter += 1
                counterList.append(counter)
            print(counterList)
            print(mean(counterList))
        elif uin == "breed":
            popArray = {}
            garry = organsim("garry", 1, [0,0], [5,[0,90],5,2], 100, "")
            larry = organsim("larry", 1, [1,1], [3,[1,91],4,3], 100, "")
            popArray["garry"] = garry
            popArray["larry"] = larry
            offSpring = breed(garry, larry, popArray)
            for x in offSpring:
                popArray[x.name] = x
            show(popArray)
        elif uin == "mage":
            popArray = {}
            garry = organsim("garry", 1, [0,0], [5,[0,90],5,2], 100)
            larry = organsim("larry", 1, [1,1], [3,[1,91],4,3], 100)
            popArray["garry"] = garry
            popArray["larry"] = larry
            print(makeGenome(garry,larry))
        elif uin == "ranran":
            for x in range(100):
                print(randrange(0,2))
        elif uin == "fight":
            garry = organsim("garry", 1, [0,0], [5,[0,90],5,2], 100)
            parry = organsim("parry", 1, [1,1], [3,[1,91],4,3], 100)
            popArray["garry"] = garry
            popArray["parry"] = parry
            fight(parry, popArray)
            show(popArray)
        elif uin == "tturn":
            garry = organsim("garry", 1, [0,0], [5,[0,90],5,1,300], 500, "")
            larry = organsim("larry", 1, [5,5], [3,[1,91],4,1,300], 500, "")
            popArray["garry"] = garry
            popArray["larry"] = larry
            plants = {}
            plants["jarry"] = plant("jarry", 1, [1,1], 300)
            plants["barry"] = plant("barry", 1, [6,6], 300)
            show(popArray)
            #show(plants)
            breedList = []
            while True:
                turn(popArray, plants, breedList)
                aliveDict = {}
                for x in popArray.values():
                    if x.lifeState == 1:
                        aliveDict[x.name] = x
                #show(aliveDict)
                show(popArray)
                #print(plants)
                #show(plants)
                posUpdate(aliveDict,plants)
                time.sleep(3)
        elif uin == "hunt":
            garry = organsim("garry", 1, [2,2], [5,[0,90],5,2], 100)
            parry = organsim("parry", 1, [5,5], [3,[1,91],4,3], 100)
            popArray["garry"] = garry
            popArray["parry"] = parry
            moveP(garry, popArray, includeSelf=1)
            show(popArray)
        elif uin == "breed1":
            garry = organsim("garry", 1, [0,0], [5,[0,90],5,1,300], 100)
            larry = organsim("larry", 1, [4,4], [3,[1,91],4,3,300], 100)
            parry = organsim("parry", 1, [5,5], [3,[1,91],4,3], 100)
            popArray["garry"] = garry
            popArray["larry"] = larry
            popArray["parry"] = parry
            breedList = [garry, larry, parry]
            bestMate = findPlants(garry.pos, breedList, organ=garry)
            print(bestMate)
            moveM(garry, larry)
            show(popArray)
        elif uin[0:5] == "vturn":
            garry = organsim("garry", 1, [0,0], [5,[0,90],5,1,300], 100, "")
            larry = organsim("larry", 1, [5,5], [3,[1,91],4,1,300], 100, "")
            popArray["garry"] = garry
            popArray["larry"] = larry
            plants = {}
            plants["jarry"] = plant("jarry", 1, [1,1], 300)
            plants["barry"] = plant("barry", 1, [6,6], 300)
            show(popArray)
            #show(plants)
            breedList = []
            for x in range(1, int(uin[5:])):
                turn(popArray, plants, breedList)
                aliveDict = {}
                for x in popArray.values():
                    if x.lifeState == 1:
                        aliveDict[x.name] = x
                show(aliveDict)
        # elif uin == "rd":
        #     print(recordData(popArray, plants))
        elif uin == "rp":
            print(recordPosition(popArray,plants))
        elif uin == "pu":
            posUpdate(popArray,plants)
        elif uin == "gwan":
            garry = organsim("garry", 1, [0,0], [5,[0,90],5,1,300], 100, "")
            larry = organsim("larry", 1, [5,5], [3,[1,91],4,1,300], 100, "")
            popArray["garry"] = garry
            plants = {}
            plants["larry"] = larry
            while True:
                wander(garry)
                wander(larry)
                posUpdate(popArray, plants)
                time.sleep(1)
        elif uin == "vgturn":
            garry = organsim("garry", 25, [0,0], [25,[0,270],25,1,300], 100, "")
            larry = organsim("larry", 25, [50,50], [25,[0,270],25,1,300], 100, "")
            popArray["garry"] = garry
            popArray["larry"] = larry
            plants = {}
            breedList = []
            while True:
                turn(popArray, plants, breedList)
                posUpdate(popArray,plants)
                show(popArray)
                time.sleep(0.5)
        elif uin == "mp":
            garry = organsim("garry", 25, [0,0], [5,[0,270],5,1,300], 100, "")
            popArray["garry"] = garry
            plants = {}
            jarry = plant("jarry", 1, [-3,-3], 100)
            plants["jarry"] = jarry
            moveP(garry,plants)
            show(popArray)
        elif uin == "mm":
            garry = organsim("garry", 25, [0,0], [25,[0,270],25,1,300], 100, "")
            larry = organsim("larry", 25, [10,10], [25,[0,270],25,1,300], 100, "")
            popArray["garry"] = garry
            popArray["larry"] = larry
            plants = {}
            posUpdate(popArray, plants)
            time.sleep(1)
            print("bean1")
            moveM(garry,larry)
            time.sleep(1)
            print("bean2")
            posUpdate(popArray, plants)
        elif uin == "trun":
            genPop(popArray, 10)
            plants = {}
            genPlant(plants, 20)
            show(popArray)
            show(plants)
            #show(plants)
            breedList = []
            print(f"popArray is {popArray}")
            posUpdate(popArray,plants)
            while True:
                turn(popArray, plants, breedList)
                aliveDict = {}
                for x in popArray.values():
                    print(f"loifeState is {x.lifeState}")
                    if x.lifeState == 1:
                        aliveDict[x.name] = x
                        print(f"{x} is x")
                #show(aliveDict)
                show(aliveDict)
                #print(plants)
                #show(plants)
                posUpdate(aliveDict,plants)
                time.sleep(3)
        elif uin == "gchill":
            garry = organsim("garry", 25, [0,0], [25,[0,270],25,1,30000000], 100, "")
            popArray["garry"] = garry
            plants = {}
            posUpdate(popArray,plants)
            breedList = []
            while True:
                turn(popArray,plants,breedList)
                posUpdate(popArray,plants)
                show(popArray)
                time.sleep(1.5)
        elif uin == "lgchill":
            garry = organsim("garry", 1, [0,0], [25,[0,270],10,1,1000], 500, "")   
            larry = organsim("larry", 1, [50,50], [25,[0,270],10,1,1000], 500, "") 
            popArray["garry"] = garry
            popArray["larry"] = larry   
            plants = {}
            posUpdate(popArray,plants)
            breedList = []
            while True:
                turn(popArray,plants,breedList)
                posUpdate(popArray,plants)
                show(popArray)
                time.sleep(1.5)
        elif uin == "run1":
            #os.system('python grpahics.py')
            garry = organsim("garry", 1, [0,0], [25,[0,270],10,1,1000], 750, "")   
            larry = organsim("larry", 1, [50,50], [25,[0,270],10,1,1000], 750, "") 
            popArray["garry"] = garry
            popArray["larry"] = larry   
            plants = {}
            posUpdate(popArray,plants)
            breedList = []
            while True:
                turn(popArray,plants,breedList)
                aliveDict = {}
                for x in popArray.values():
                    if x.lifeState == 1:
                        aliveDict[x.name] = x
                posUpdate(aliveDict,plants)
                show(aliveDict)
                time.sleep(1.5)  
        elif uin == "sim1":
            # garry = organsim("garry", 1, [0,0], [25,[0,270],15,5,1000], 750, "")   
            # larry = organsim("larry", 1, [50,50], [25,[0,270],15,5,1000], 750, "") 
            # popArray["garry"] = garry
            # popArray["larry"] = larry   
            genPop(popArray, 10)
            plants = {}
            genPlant(plants ,30)
            posUpdate(popArray,plants)
            breedList = []
            while True:
                turn(popArray,plants,breedList)
                aliveDict = {}
                for x in popArray.values():
                    if x.lifeState == 1:
                        aliveDict[x.name] = x
                posUpdate(aliveDict,plants)
                show(aliveDict)
                time.sleep(1) 

        elif uin == "smooth":
            garry = organsim("garry", 1, [0,0], [25,[0,270],10,1,1000], 500, "")   
            larry = organsim("larry", 1, [50,50], [25,[0,270],10,1,1000], 500, "") 
            popArray["garry"] = garry
            popArray["larry"] = larry   
            plants = {}
            smoothposUpdate(popArray,plants, 24)
            wander(garry)
            smoothposUpdate(popArray,plants, 24)
        elif uin == "sStep":
            print(smoothStep([5,13], [10,10], 9))
        elif uin == "ss1":
            garry = organsim("garry", 1, [0,0], [25,[0,270],10,1,1000], 500, "")   
            larry = organsim("larry", 1, [50,50], [25,[0,270],10,1,1000], 500, "") 
            popArray["garry"] = garry
            popArray["larry"] = larry   
            plants = {}
            posUpdate(popArray,plants)
            wander(garry)
            smoothSteper(popArray, plants, 10)
        elif uin == "asdf":
            garry = organsim("garry", 1, [0,0], [25,[0,270],10,1,1000], 500, "")   
            larry = organsim("larry", 1, [50,50], [25,[0,270],100,1,1000], 500, "") 
            popArray["garry"] = garry
            popArray["larry"] = larry   
            plants = {}
            posUpdate(popArray,plants)
            garry.pos = move(garry.pos, 150, dgTR(45))
            smoothPosUpdater(popArray, plants, 1, 3)
        elif uin == "tb":
            timingBelt(5, 10)
        elif uin == "rs":
            garry = organsim("garry", 1, [0,0], [25,[0,270],10,1,1000], 500, "")   
            larry = organsim("larry", 1, [50,50], [25,[0,270],100,1,1000], 500, "") 
            popArray["garry"] = garry
            popArray["larry"] = larry   
            plants = {}
            posUpdate(popArray,plants)
        elif uin == "fa":
        # y = a(x-h)^2 + k
            print(findA(50, (0,1), (0,5)))
        elif uin == "fy":
            jarry = plant("jarry", 1, [-3,-3], 100, 1)
            for x in range(10):
                print(findY(jarry))
                jarry.age += 1
        elif uin == "pT":
            breedList = []
            popArray = {}
            plants = {}
            genPlant(plants, 10)
            for tempVar in range(10):
                turn(popArray, plants, breedList)
                show(plants)
        elif uin == "lc":
            litterChance(2)
        elif uin == "mG":
            garry = organsim("garry", 25, 0, "M", [5,1,26,2,30, 3], 100, "")
            larry = organsim("larry", 25, 0, "F" , [25,1,25,1,300, 4], 100,  "")
            print(newGenome(garry, larry))
        elif uin == "repro":
            garry = organsim("garry", 25, [0,0], "M", [5,1,26,2,30, 3], 100, "")
            larry = organsim("larry", 25, [0,0], "F" , [25,1,25,1,300, 4], 100,  "")
            popArray = {"garry" : garry, "larry" : larry}
            print(reproduce(garry, larry, popArray))
            intergrateOffspring(reproduce(garry, larry, popArray), popArray)
            show(popArray)
        elif uin == "sctst":
            popArray = {}
            garry = organsim("garry", 25, [0,0], "M", [5,1,26,2,30, 3], 100, "")
            genPop(popArray,3)
            score = scoreMate(garry, popArray)
            print(score)
            nscore = numberScoreMate(score)
            print(nscore)
        elif uin == "avgSkill":
            popArray = {}
            genPop(popArray,5)
            print(averageSkill(popArray))
        elif uin == "bmate":
            popArray = {}
            garry = organsim("garry", 25, [0,0], "M", [5,1,26,2,30, 3], 100, "")
            genPop(popArray,3)
            print(findBestScoredMate(garry, popArray))
        elif uin == "dos":
            popArray = {}
            mateList = []
            genPop(popArray,5)
            for x in popArray.values():
                mateList.append(x)
            print(dictOfScore(mateList,popArray))
        elif uin == "sortS":
            popArray = {}
            mateList = []
            genPop(popArray,5)
            for x in popArray.values():
                mateList.append(x)
            a = sortScore(dictOfScore(mateList,popArray))
            show(popArray)
            print(a)
        elif uin == "mmr":
            popArray = {}
            mateList = []
            genPop(popArray,5)
            for x in popArray.values():
                mateList.append(x)
            bean = dictOfScore(mateList,popArray)
            a = sortScore(dictOfScore(mateList,popArray))
            show(popArray)
            b = matchMakerList(a)
            c = matchMaker(b, bean)
            print(c)
            #testing2
        # else:
        #     function(uin)

        inputTaken = True

# tester = organsim("Tester", 1, [1,1], [1,1,1,1,1,1], 32)
# popArray = {}
# popArray = genPop(popArray,10)
# print(popArray)
# show(popArray)
if __name__ == '__main__':
    popArray = {}
    t1 = Thread(target=afk)
    #t2 = Thread(target=execute,args=(popArray,))

    t1.start()
    #t2.start()
    print("They are started")
    execute(popArray)
    #t2.join()  # interpreter will wait until your process get completed or terminated
    thread_running = False
    print('The end')


    # while True:
    #     if halt == True:
    #         break

    # uin = input()
    # if uin == "exit":
    #     break
    # elif uin == "rtn":
    #     uin = input("Input number to be rtn: ")
    #     print(romToNum(uin))
    # elif uin == "ntr":
    #     uin = input("Input a number to be ntr: ")
    #     print(numToRom(uin))
    # elif uin == "gpt":
    #     popArray = genPop(popArray,10)
    #     show(popArray)
    # elif uin == "rna":
    #     rom = input("Input rom ")
    #     num = input("Input num ")
    #     print(romNumAdd(rom,num))

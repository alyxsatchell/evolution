BASE_SYSTEM = 3
def listToStr(l):
    string = ""
    for x in l:
        string += str(x) + ","
    return string

def strToList(s):
    l = []
    for x in s:
        l.append(s)
    return l

def numToBinary(num):
    quot = int(num)
    bin = []
    binary = ""
    while True:
        if quot <= 0:
            break
        remain = quot % BASE_SYSTEM
        bin.append(remain)
        quot = quot // BASE_SYSTEM
    bin.reverse()
    for x in bin:
        binary += str(x)
    return binary

def binaryToNum(binary):
    bin = []
    num = []
    for x in str(binary):
        bin.append(x)
    bin.reverse()
    for index, x in enumerate(bin):
        num.append(int(x) * (BASE_SYSTEM ** index))
    return sum(num)

def stringToNum(string):
    num = []
    for x in string:
        num.append(ord(x))
    return num

def stringToBin(string):
    num = stringToNum(string)
    bin = []
    for x in num:
        bin.append(numToBinary(x))
    return bin

def toBin(string):
    bin = stringToBin(string)
    return listToStr(bin)

def toWord(binString):
    words = ""
    prevIndex = 0
    for index,x in enumerate(binString):
        if x == ",":
            #print(f"stuff os {int(binString[prevIndex:index])}")
            words += chr(int(binaryToNum(binString[prevIndex:index])))
            prevIndex = index + 1
    return words

print(numToBinary(16))
print("Note all binary needs to have only numbers with \"whole letters\" seperated by \",\"")
while True:
    uin = input("Input a command:\n").lower()
    if uin == "exit":
        break
    elif uin == "encode" or uin == "e":
        uin = input("Input something to be turned into binary or set base system:\n")
        print(toBin(uin))
    elif uin == "decode" or uin == "d":
        uin = input("Input binary or other set base system to be decoded into unicode:\n")
        print(toWord(uin))
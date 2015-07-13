from collections import OrderedDict
testcases = int(input())

def untangle(w, e):
    key = list(OrderedDict.fromkeys(w))
    alphabet = []
    for x in range(ord("A"), ord("Z")+1):
        addToAlphabet = True
        for y in key:
            if (x == ord(y)):
                addToAlphabet = False

        if (addToAlphabet == True):
            alphabet.append(chr(x))

    maps = []
    for x in key:
        maps.append([x])

    length = len(key)
    c = 0
    for x in alphabet:
        maps[c].append(x)
        c = c + 1
        if (c > (length - 1)):
            c = 0
    temp = key.copy()
    temp.sort()
    ordMaps = []
    for x in range(length):
        target = temp[x]
        for m in maps:
            if (m[0] == target):
                ordMaps.append(m)
                break
    #flatten maps
    keyAlpha = []
    for x in ordMaps:
        for y in x:
            keyAlpha.append(y)

    offset = ord('A')
    kaLen = len(keyAlpha)

    for t in e:
        for x in range(kaLen):
            if (t == keyAlpha[x]):
                print (chr(offset + x), end="")
                break
            if (t == " "):
                print (" ", end="")
                break




for x in range(testcases):
    word = input()
    enc = input()
    untangle(word, enc)
    print ("")

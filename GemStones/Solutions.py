import collections

testcases = int(input())
firstElement = input()
commonalities = collections.OrderedDict()
for n in firstElement:
    commonalities[n] = 1

for testcase in range(testcases-1):
    otherElement = input()
    uniques = collections.OrderedDict()
    for z in otherElement:
        uniques[z] = 0

    for x in commonalities:
        for y in uniques:
            if (x == y):
                commonalities[x] = commonalities[x] + 1

ans = 0
for x in commonalities:
    if (commonalities[x] == testcases):
        ans = ans + 1

print (ans)

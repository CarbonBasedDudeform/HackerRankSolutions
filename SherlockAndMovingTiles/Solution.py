#solution for HackerRank problem:
#   https://www.hackerrank.com/challenges/sherlock-and-moving-tiles


import math

blah = input()
blah = blah.split()
L = int(blah[0])
L2 = L*L
S1 = int(blah[1])
S2 = int(blah[2])

Q = int(input())

def ReadInQs():
    qs = []
    for x in range(Q):
        qs.append(int(input()))

    return qs

qs = ReadInQs() #note: could do the sherlock() as input is read in, turning the cur 2N into an N solution

squaresHyp = math.sqrt(L2+L2)
rate = S2-S1
def sherlock(x):
    d = squaresHyp - math.sqrt(x+x)
    t = abs(d/rate)
    return t

for q in qs:
    print (sherlock(q))

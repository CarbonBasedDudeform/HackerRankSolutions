from fractions import gcd
testcases = int(input())

def a(x,y):
    if (x == y): #already largest square
        print (1)    #no cuts
        return

    factor = gcd(x, y)
    print (int((x/factor)*(y/factor))) #conv. to int necessary due to site not recognising 1 as 1.0
    return

for q in range(testcases):
    i = input()
    i = i.split()
    x = int(i[0])
    y = int(i[1])

    a(x,y)

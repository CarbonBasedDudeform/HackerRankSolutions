def setup(str):
    temp = str.split()
    temp = list(map(int, temp))
    return temp

actual = setup(input())
expected = setup(input())

def EigenDate(vals):
    return vals[0] + (vals[1]*30) + (vals[2]*365)

eigenActual = EigenDate(actual)
eigenExpected = EigenDate(expected)

deltaDay = actual[0] - expected[0]
deltaMonth = actual[1] - expected[1]
deltaYear = actual[2] - expected[2]

rate = 0
deltaToBeUsed = 0

if (eigenExpected - eigenActual) < 0:
    if (deltaDay <= 0 and deltaMonth <= 0 and deltaYear <= 0):
        rate = 0
    elif (deltaMonth <= 0 and deltaYear <= 0):
        rate = 15
        deltaToBeUsed = deltaDay
    elif (deltaYear <= 0):
        rate = 500
        deltaToBeUsed = deltaMonth
    else:
        rate = 10000
        deltaToBeUsed = 1



print (rate * deltaToBeUsed)

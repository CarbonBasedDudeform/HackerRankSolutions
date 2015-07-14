numTestCases = int(input())

for x in range(numTestCases):
    temp = input()
    temp = temp.split()

    numStudents = int(temp[0])
    threshold = int(temp[1])
    arrivalTimes = input()
    arrivalTimes = arrivalTimes.split(' ')
    sumIs = 0
    for x in arrivalTimes:
        if (int(x) <= 0):
            sumIs += 1

    if sumIs < threshold:
        print("YES")
    else:
        print("NO")

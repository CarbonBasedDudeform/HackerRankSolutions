testCases = int(input())

for n in range(testCases):
    points = input()
    points = points.split(" ")
    x = (int(points[0]), int(points[1]))
    y = (int(points[2]), int(points[3]))

    diffHorz = y[0] - x[0]
    diffVert = y[1] - x[1]

    symP = (y[0] + diffHorz, y[1] + diffVert)
    print("{0} {1}".format(symP[0], symP[1]))

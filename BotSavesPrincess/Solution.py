#!/usr/bin/python
def findChar(grid, char):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if (grid[y][x] == char):
                return (x,y)
    return (-1, -1)
def findM(grid):
    return findChar(grid, 'm')

def findP(grid):
    return findChar(grid, 'p')

def makeGoodGrid(grid):
    actualGrid =[]
    for x in grid:
        y = list(x)
        actualGrid.append(y)
    return actualGrid

def EndGameCheck(cX, cY, pPos):
    return pPos[0] != cX or pPos[1] != cY
def displayPathtoPrincess(n,grid):
    grid = makeGoodGrid(grid)
    pPos = findP(grid)
    mPos = findM(grid)
    cPosX = mPos[0]
    cPosY = mPos[1]
    flip = False
    while(EndGameCheck(cPosX, cPosY, pPos)):
        if cPosX == pPos[0]:
            flip = False
        if cPosY == pPos[1]:
            flip = True
        if (flip):
            flip = False
            if cPosX < pPos[0]:
                cPosX += 1
                print("RIGHT")
            else:
                cPosX -= 1
                print("LEFT")
        else:
            flip = True
            if cPosY < pPos[1]:
                cPosY += 1
                print("DOWN")
            else:
                cPosY -= 1
                print("UP")


#print all the moves here
m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m,grid)

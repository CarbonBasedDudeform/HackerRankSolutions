height = int(input())

for x in range(1, height+1):
    for z in range(height-x):
        print(" ", end="")
    for y in range(x):
        print ("#", end="")

    print ("")
    

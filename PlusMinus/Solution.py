total = int(input())
nums = input()
nums = nums.split()

totalPos = 0
totalNeg = 0
totalZero = 0

for x in nums:
    x = int(x)
    if x > 0:
        totalPos += 1
    elif x < 0:
        totalNeg += 1
    else:
        totalZero += 1

print (totalPos/total)
print (totalNeg/total)
print (totalZero/total)

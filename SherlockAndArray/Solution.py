testcases = int(input())
def determine(nums):
    l = len(nums)
    total = 0
    for x in nums:
        total += x
        
    runningTotal = 0
    for x in nums:
        total -= x

        if ((total - runningTotal) == 0):
            return "YES"

        runningTotal += x

    return "NO"

for tc in range(testcases):
    input() #throwaway, length of array, can use in determine() to avoid calc of length but more fiddly
    nums = input()
    nums = list(map(int, nums.split()))
    print (determine(nums))

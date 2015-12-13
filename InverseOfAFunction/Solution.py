throwaway = input()
vals = input()
vals = vals.split()
vals = list(map(int, vals))

hackyMap = {}
hackyInverse = {}
#absolute bellends starting from 1 instead of 0

for val in range(len(vals)):
    hackyMap[val+1] = vals[val]
    hackyInverse[vals[val]] = val+1

for v in range(1, len(hackyInverse)+1):
    if (v in hackyInverse):
        print(hackyInverse[v])

throwaway = input()
vals = input()
vals = vals.split()
vals = list(map(int, vals))

#Determins wether it is a bijective function by ensuring that for any case f(v) = f(u) => u = v
#in plain english, if any of the values are the same, then there are two values, x and y, which both give the same result called r.
#this means there cannot be an inverse function as there is ambiguity in f'(r), both f'(r) = x and f'(r) = y are true but x != y so you have f'(r) != f'(r)
res = "YES"
for subject in range(len(vals)):
    if (res == "YES"):
        for target in range(subject+1, len(vals)): #only checks the rest of the set as the first part has already been checked against the rest. There's no point checking if the mid item is the same as the first item as it would have been found when checking the first item against the mid item.
            if (vals[subject] == vals[target]):
                res = "NO"
                break
print(res)

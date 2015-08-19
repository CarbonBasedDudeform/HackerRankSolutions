first = input()
second = input()

def initms(string):
    m = {}
    for x in string:
        if x not in m:
            m[x] = 1
        else:
            m[x] += 1

    return m

m1 = initms(first)
m2 = initms(second)

def count(m, oM):
    ans = 0
    for x in m:
        try:
            ans = ans + max(0, m[x] - oM[x])
        except:
            ans = ans + m[x]
    return ans

ans = count(m1, m2) + count(m2, m1)

print(ans)

testcases = int(input())

def setup(s):
    m = {}
    for x in s:
        if x not in m:
            m[x] = 1
        else:
            m[x] += 1

    return m

def count(m, m2):
    ans = 0
    for x in m:
        if x not in m2:
            ans += m[x]
        elif m[x] != m2[x]:
            ans += max(0, m[x] - m2[x])
    return ans

for testcase in range(testcases):
    string = input()
    if len(string) % 2 != 0:
        print("-1")
    else:
        letterFreq1 = setup(string[:len(string)//2])
        letterFreq2 = setup(string[len(string)//2:])
        print(count(letterFreq1, letterFreq2))

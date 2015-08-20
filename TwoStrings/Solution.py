def analyse(s1, s2):
    #find at least one common letters
    for x in s1:
        if x in s2:
            return "YES"

    for x in s2:
        if x in s1:
            return "YES"

    return "NO"

testcases = int(input())
for testcase in range(testcases):
    str1 = input()
    str2 = input()
    print (analyse(str1, str2))
    

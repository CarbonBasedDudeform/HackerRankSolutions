testcases = int(input())

for tests in range(testcases):
    numTowns = int(input())
    routes = input()
    routes = routes.split()
    routes = list(map(int, routes))
    ans = 1
    for x in routes:
        ans *= x

    print (ans % 1234567)

testcases = int(input())

for testcase in range(testcases):
    x = int(input())
    Sn = 1
    if x > 1:
        Sn = pow(x, 2) #small analysis of series shows difference between N and N+1 is always 2, with N = 0, answer is 1, N = 1 answer is 1, actual formula Sn = 1 + N^2, but hr only considers N > 0, => Sn = N^2

    print(Sn % (pow(10, 9) + 7)) #could inline to avoid recalc. of pow. laziness though.

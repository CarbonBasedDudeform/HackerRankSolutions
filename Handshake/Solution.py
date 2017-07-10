#!/bin/python3

import sys

def NumHandshakes(n):
    return (n*(n-1)) // 2
T = int(input().strip())
for a0 in range(T):
    N = int(input().strip())
    print(NumHandshakes(N))

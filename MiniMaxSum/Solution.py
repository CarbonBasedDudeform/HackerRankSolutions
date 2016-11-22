#!/bin/python

import sys

def fourSmallestSum(arrs):
    largest = 0 - sum(arrs)
    for x in arrs:
        if (x > largest):
            largest = x
    copy_arrs = list(arrs)
    copy_arrs.remove(largest)
    return sum(copy_arrs)

def fourLargestSum(arrs):
    smallest = sum(arrs)
    for x in arrs:
        if (x < smallest):
            smallest = x
    copy_arrs = list(arrs)
    copy_arrs.remove(smallest)
    return sum(copy_arrs)

a,b,c,d,e = input().strip().split(' ')
arrs = [int(a),int(b),int(c),int(d),int(e)]
print(str(fourSmallestSum(arrs)) + " " + str(fourLargestSum(arrs)))

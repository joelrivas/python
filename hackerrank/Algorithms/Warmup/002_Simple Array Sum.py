#!/bin/python3

import sys

def simpleArraySum(n, ar):
    # Complete this function
    i = 0
    j = 0
    while i < n:
        j += ar[i]
        i += 1
    
    return j

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)


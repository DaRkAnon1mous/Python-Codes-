#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    c = 0
    d = 0
    h = 0
    l = len(arr)
    for i in range(l):
        if arr[i] > 0:
            c +=1
        elif arr[i] < 0:
            d += 1
        else:
            h += 1
    print(c/l)
    print(d/l)
    print(h/l)
                   

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

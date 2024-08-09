#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    sumi = 0
    sumo = 0
    n = len(arr)
    for i in range(n-1):
        sumi += arr[i]
    for j in range(n-1,0,-1):
        sumo += arr[j]
    print (sumi , sumo)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

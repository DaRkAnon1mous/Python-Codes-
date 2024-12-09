#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
from functools import reduce

# Function to calculate the LCM of two numbers
def lcm(x, y):
    return x * y // math.gcd(x, y)

# Function to calculate the LCM of a list of numbers
def lcm_list(lst):
    return reduce(lcm, lst)

# Function to calculate the GCD of a list of numbers
def gcd_list(lst):
    return reduce(math.gcd, lst)
    
def getTotalX(a, b):
   lcm_a = lcm_list(a)   # Step 1: LCM of list A
   gcd_b = gcd_list(b)   # Step 2: GCD of list B
   count = 0
   for i in range(lcm_a, gcd_b + 1, lcm_a):
       if gcd_b % i == 0:
           count += 1
   return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()

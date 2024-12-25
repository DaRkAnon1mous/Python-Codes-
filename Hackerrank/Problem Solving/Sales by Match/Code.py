#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    sortedl = sorted(ar)  # Sort the array
    count = 0
    i = 0  
    while i < len(sortedl) - 1:  
        if sortedl[i] == sortedl[i + 1]:  
            count += 1  
            sortedl.pop(i)  
            sortedl.pop(i)
        else:
            i += 1  # Move to the next element
    return count
        
        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

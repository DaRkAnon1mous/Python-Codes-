#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#



def birthday(s,d,m):
    count = 0
    # Traverse the chocolate bar with a sliding window of size `m`
    for i in range(len(s) - m + 1):
        # Calculate the sum of the current segment
        if sum(s[i:i + m]) == d:
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()

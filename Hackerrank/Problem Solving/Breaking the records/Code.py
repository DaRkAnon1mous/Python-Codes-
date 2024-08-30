#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    hscore = scores[0]
    lscore = scores[0]
    count1 = 0
    count2 = 0
    for i in range(1, len(scores)):
        if scores[i] >hscore:
            hscore=scores[i]
            count1+=1
        elif scores[i] < lscore:
            lscore = scores[i]
            count2 += 1
        else:
            continue
    return count1, count2
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

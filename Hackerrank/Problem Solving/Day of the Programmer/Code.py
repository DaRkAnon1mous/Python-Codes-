#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import date

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    if year<1918:
        if year%4==0:
            dt = date(year,9,12)
            fr = dt.strftime('%d.%m.%Y')
            return fr
        else:
            dt = date(year,9,13)
            fr = dt.strftime('%d.%m.%Y')
            return fr
    elif year>1918:
        if (year%400==0) or (year%4==0 and year%100!=0):
            dt = date(year,9,12)
            fr = dt.strftime('%d.%m.%Y')
            return fr
        else:
            dt = date(year,9,13)
            fr = dt.strftime('%d.%m.%Y')
            return fr
    else:
        dt = date(year,9,26)
        fr = dt.strftime('%d.%m.%Y')
        return fr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()

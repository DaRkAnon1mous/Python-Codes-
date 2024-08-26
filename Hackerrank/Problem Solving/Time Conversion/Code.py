#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime,timedelta
#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    date1 = datetime.strptime(s,'%I:%M:%S%p')
    
    newdate = date1.strftime('%H:%M:%S')
    return newdate

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    l = len(grades)
    z = 0
    k = 0
    arr2 = []
    for i in range(l):
        if grades[i] < 37 :
            z = grades[i]
            arr2.append(z)
        else:
            if grades[i] % 5 == 0:
                z = grades[i]
                arr2.append(z)
            else:
                z = (grades[i] + 5) - (grades[i] % 5)
                if z - grades[i] < 3:
                    arr2.append(z)
                else:
                    k = grades[i]
                    arr2.append(k)
    return arr2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

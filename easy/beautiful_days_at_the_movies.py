#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def _reverse(v) -> int:
    n = str(v)
    s = ""
    for i in range((len(n)-1), -1, -1):
        s += n[i]
        
    return int(s)

def beautifulDays(i, j, k):
    b = []
    for v in range(i, j+1):
        t = (v-_reverse(v))/k
        if t%1 == 0:
            b.append(t)
            
    return len(b)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()

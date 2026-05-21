#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    tp = math.ceil(n/2)
    if n%2 == 0:
        tp += 1
        
    dp = math.ceil(p/2)
    if p%2 == 0:
        dp += 1

    fs = 0
    for s in range(1, (int(tp)+1)):
        if s == dp:
            fs = s-1
            break
        
    fe = 0
    for s in range((int(tp)+1), 1, -1):
        if s == dp:
            fe = tp-s
            break

    return fs if fs <= fe else fe

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()

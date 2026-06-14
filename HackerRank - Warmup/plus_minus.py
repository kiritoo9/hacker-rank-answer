#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    counts = [0, 0, 0]
    
    # counting
    for v in arr:
        if v > 0:
            counts[0] += 1
        elif v < 0:
            counts[1] += 1
        else:
            counts[2] += 1
            
    # dividing
    for c in counts:
        print(round(c/len(arr), 6))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

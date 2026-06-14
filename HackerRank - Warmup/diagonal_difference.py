#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    primary_values = []
    primary_pos = [0, 0]
    
    secondary_values = []
    secondary_pos = [0, len(arr)-1]
    
    for _ in arr:
        primary_values.append(arr[primary_pos[0]][primary_pos[1]])
        primary_pos[0] += 1
        primary_pos[1] += 1
        
        secondary_values.append(arr[secondary_pos[0]][secondary_pos[1]])
        secondary_pos[0] += 1
        secondary_pos[1] -= 1
    
    return abs(sum(primary_values) - sum(secondary_values))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

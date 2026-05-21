#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    birds = dict.fromkeys(arr)
    highest = 0
    for v in list(birds):
        total = arr.count(v)
        if total > highest:
            highest = total
        
        birds[v] = total

    final = []
    for j in birds:
        if birds[j] == highest and j not in final:
            final.append(j)
    
    if final:
        return sorted(final)[0]
    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

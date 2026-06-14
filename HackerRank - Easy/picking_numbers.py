#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    a = sorted(a)
    storage = []
    sess = []
    for i, v in enumerate(a):
        check = {
            "a": ((i+1)<len(a) and abs(v-(a[i+1]))<=1),
            "b": all([abs(v-s)<=1 for s in sess])
        }
        
        if all(check.values()) or check.get("a") is False and check.get("b") is True:
            sess.append(v)
            if i>=len(a)-1:
                storage.append(len(sess))
        else:
            storage.append(len(sess))
            sess = [v]

    return max(storage)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    prefix = 0
    for i in range(len(s)):
        if i >= len(t):
            continue
        
        if s[i] == t[i]:
            prefix += 1
        else:
            break
    
    if prefix==len(t):
        return "No" if len(s[prefix:len(s)])>k else "Yes"
    elif len(s)<len(t):
        c = len(s)-prefix
        return "Yes" if c<k else "No"
    else:
        return "Yes" if len(s[prefix:])+len(t[prefix:]) == k else "No"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()

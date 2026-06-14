#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr = sorted(arr)
    
    min_value = sum(arr[0:(len(arr)-1)])
    max_value = sum(arr[1:])
    
    print(min_value, max_value)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

#!/bin/python3

import math
import os
import random
import re
import sys
import calendar

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    gregorian_start = 1918
    max_month = 9
    total_d = 0
    is_julian = True if year < gregorian_start else False

    for m in range(1, max_month):
        total_m = calendar.monthrange(year, m)[1]
        
        if m == 2:
            if is_julian is True and year%4 == 0:
                total_m = 29
            elif year%4 == 0 and (year%100 != 0 or year%400 == 0):
                total_m = 29
            else:
                total_m = 28
            
            # check transision calendar system
            if year == gregorian_start:
                total_m -= 13
            
        total_d += total_m
        
    c = 256-total_d
    return f"{c}.09.{year}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()

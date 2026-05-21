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
    max_divide = 3
    minimum_grade = 38
    scores = []
    
    for g in grades:
        if g >= minimum_grade:
            multiple_by_five = math.ceil(g/5) * 5
            scores.append(
                multiple_by_five if (multiple_by_five - g) < max_divide else g
            )
        else:
            scores.append(g)
            
    return scores
    

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

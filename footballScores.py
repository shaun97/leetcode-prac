#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'counts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY teamA
#  2. INTEGER_ARRAY teamB
#

def counts(teamA, teamB):
    # Write your code here
    # 1) Sort team A scores
    # 2) Iterate through team B scores and do a binary search to find the smallest element greater than 
    # that particular team B's score
    
    # 1) sort
    teamA.sort()
    res = []

    for i in teamB:
        # Binary search here
        left, right = 0, len(teamA) - 1
        
        # handle when teamB score is larger than everyone
        if i > teamA[-1]:
            res.append(len(teamA))
            continue
        elif i < teamA[0]:
            res.append(0)
            continue
            
        while left < right:
            mid = left + (right - left) // 2
            if teamA[mid + 1] <= i:
                left = mid + 1
            elif teamA[mid] > i:
                right = mid
            elif teamA[mid + 1] > i and teamA[mid] <= i:
                res.append(mid + 1)
                break
            else:
                print("test")
                break
                
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    teamA_count = int(input().strip())

    teamA = []

    for _ in range(teamA_count):
        teamA_item = int(input().strip())
        teamA.append(teamA_item)

    teamB_count = int(input().strip())

    teamB = []

    for _ in range(teamB_count):
        teamB_item = int(input().strip())
        teamB.append(teamB_item)

    result = counts(teamA, teamB)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

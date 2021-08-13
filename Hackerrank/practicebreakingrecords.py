#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    lowest=scores[0]
    highest=scores[0]
    ma=0
    mi=0
    
    for i in scores:
        if i==scores[0]:
            #print("passed")
            pass
        else:
            #print(i)
            if i> highest:
                highest=i
                ma+=1
            elif i<lowest:
                lowest=i
                mi+=1
    
   
    
    return ma,mi

if __name__ == '__main__':
    

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
    print(result)

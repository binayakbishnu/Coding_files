#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    d={}
    c=0
    for i in ar:
        if i in d:
            d[i]+=1
        else:
            d[i] = 1
            
    for key in d.keys():
        if d[key]%2!=0 and (d[key])-1 !=0:
            d[key]-=1

        if d[key]%2==0:
            c+=d[key]//2
            print(d[key], math.log(d[key],2))
    print(d)
    return c
            
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    #fptr.write(str(result) + '\n')
    print(str(result) + '\n')
    #fptr.close()
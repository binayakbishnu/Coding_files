#!/bin/python3

import math
import os
import random
import re
import sys


arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))
        
#print(arr[2][5])
s=0
s1=[]
for x in range(4):
    for i in range(0,4):
        s=0
        for j in range(i,i+3,1):
            #print(j)
            s+=arr[x][j]
            s+=arr[x+2][j]
        s+=arr[x+1][i+1]
        s1.append(s)
        #print(s)
        
    #print("x=",x)
    #print("--")
print(max(s1))
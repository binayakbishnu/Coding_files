import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    s=0
    for i in bill:
        if i!=bill[k]:
            s+=i
    s1=s//2
    if b==s1:
        print("Bon Appetit")
    else:
        print(b-s1)



n = int(input())
k = int(input())
bill = list(map(int, input().rstrip().split()))
b = 249191240
bonAppetit(bill, k, b)

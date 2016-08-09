""" 
Problem:

A permutation of length nn is an ordering of the positive integers {1,2,…,n}{1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 55.

Given: A positive integer n≤7.

Return: The total number of permutations of length nn, followed by a list of all such permutations (in any order).

"""

import itertools
import math
import re

print("Write down the lenght of the sequence you want to permute")
s = int(input())

o=[0]*s

for n in range(0,s):
        o[n]=n+1
        
x=list(itertools.permutations(o))
x=''.join(map(str, x))
x= re.findall(r'\d+', x)

print( math.factorial(s))
for i in range(0,int(len(x)/s)):
        for y in range(0,s):
                print(x[i*s +y], end=" ")
        print("")

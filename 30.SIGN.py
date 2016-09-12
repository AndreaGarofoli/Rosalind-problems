"""

Problem:


A signed permutation of length nn is some ordering of the positive integers {1,2,…,n} in which each integer is then provided with either a positive or negative sign (for the sake of simplicity, we omit the positive sign). For example, π=(5,−3,−2,1,4) is a signed permutation of length 5.

Given: A positive integer n≤6.

Return: The total number of signed permutations of length n, followed by a list of all such permutations (you may list the signed permutations in any order).

"""

import itertools
import math
import re

print("Write down the lenght of the sign permutation")

n = int(input())

i=[]

for x in range(1,n+1):
	i.append(x)
	i.append(-x)

t=list(s for s in itertools.permutations(i, n) if len(set(map(abs, s))) == len(s))
print(len(t))

t='\n'.join(str(v) for v in t)


print(re.sub("[(),]","",t))




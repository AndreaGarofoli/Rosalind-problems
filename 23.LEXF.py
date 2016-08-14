""" 
Problem:

Assume that an alphabet AA has a predetermined order; that is, we write the alphabet as a permutation A=(a1,a2,…,ak), where a1<a2<⋯<ak. For instance, the English alphabet is organized as (A,B,…,Z).

Given two strings ss and tt having the same length nn, we say that ss precedes tt in the lexicographic order (and write s<Lexts<Lext) if the first symbol s[j] that doesn't match t[j] satisfies sj<tj in A.

Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer nn (n≤10).

Return: All strings of length nn that can be formed from the alphabet, ordered lexicographically.

"""

import itertools

a = open("in_23.txt","r").read().split('\n')

o= "".join(sorted(a[0].split(" ")))
l= int(a[1])

for p in itertools.product(o, repeat=l):
        print("".join(p))
        

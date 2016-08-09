"""

Problem:


Given two strings s and t of equal length, the Hamming distance between ss and tt, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t)d.

"""

s = open("in_6.txt","r").read().split('\n')


m=0


for x in enumerate(s[0]):
    n= x[0]
    if s[0][n] != s[1][n]:
        m=m+1

print (m)




"""

Problem:


For DNA strings s1 and s2 having the same length, their transition/transversion ratio R(s1,s2) is the ratio of the total number of transitions to the total number of transversions, where symbol substitutions are inferred from mismatched corresponding symbols as when calculating Hamming distance (see “Counting Point Mutations”).

Given: Two DNA strings s1s1 and s2 of equal length (at most 1 kbp).

Return: The transition/transversion ratio R(s1,s2).

"""

from Bio import SeqIO


s=[]
u=["A", "G"]
i=["C", "T"]
t=0
v=0



for seq_record in SeqIO.parse("in_29.txt", "fasta"):
    s.append(list(str(seq_record.seq)))

m=0

for x in enumerate(s[0]):
    n= x[0]
    if s[0][n] != s[1][n]:
        if s[0][n] in u and s[1][n] in u: t+=1
        elif s[0][n] in i and s[1][n] in i: t+=1
        else: v+=1

print (round(t/v, 11))



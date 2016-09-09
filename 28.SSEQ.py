""" 
Problem:

A partial permutation is an ordering of only k objects taken from a collection containing nn objects (i.e., k≤n). For example, one partial permutation of three of the first eight positive integers is given by (5,7,2).

The statistic P(n,k) counts the total number of partial permutations of k objects that can be formed from a collection of nn objects. Note that P(n,n) is just the number of permutations of nn objects, which we found to be equal to n!=n(n−1)(n−2)⋯(3)(2) in “Enumerating Gene Orders”.

Given: Positive integers nn and kk such that 100≥n>0 and 10≥k>0.

Return: The total number of partial permutations P(n,k), modulo 1,000,000.

"""


from Bio import SeqIO

b=""
s=""
i=0


for seq_record in SeqIO.parse("in_28.txt", "fasta"):
    if b=="": b=list(str(seq_record.seq))
    else: s=list(str(seq_record.seq))

r=[]

for n in range(0,len(b)):
    if i>(len(s)-1): break
    else:
        if b[n]==s[i]:
            r.append(str(n+1))
            i+=1
        


print(" ".join(r))

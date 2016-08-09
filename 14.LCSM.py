        
"""

Problem

A common substring of a collection of strings is a substring of every member of the collection. We say that a common substring is a longest common substring if there does not exist a longer common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGGTATA", but it is not as long as possible; in this case, "GTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)


"""

from Bio import SeqIO


def xseq(ts,sub,lu):
    mm=0
    for seq_record in SeqIO.parse("in_14.txt", "fasta"):
        if ts not in seq_record.seq: return(None)
    return(ts)


l=99999999999999999999999999999999999999
ss=""

lu=0

for seq_record in SeqIO.parse("in_14.txt", "fasta"):
    lu+=1
    if l > len(seq_record.seq): 
        l= len(seq_record.seq)
        ss=seq_record.seq

ts=""
db=0
xc="-"


for n in range(0,l):
    sub=l-n
    y=0
    for x in range(sub,l+1):
        #print(x,n,sub)        
        ts=ss[0+y:x]
        xc=xseq(ts,sub,lu)
        y+=1
        if xc != None:
            break
    else:
        continue
    break

print(xc)
        
        





"""

Problem:

After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.

Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)

"""


import re
from Bio import SeqIO

i=0
ex=[]


for seq_record in SeqIO.parse("in_20.txt", "fasta"):
    if i == 0: 
            a = "".join(seq_record.seq)
            #print(a)
    else:
        b="".join(seq_record.seq)
        ex.append(b)

    i=1

for i in ex:
    a = re.sub(i, '', a)


n=a

c= [["A","GCU","GCA","GCC","GCG"],["C","UGC","UGU"],["D","GAU","GAC"],["E","GAA","GAG"],["F","UUC","UUU"],["G","GGU","GGG","GGC","GGA"],["H","CAC","CAU"],["I","AUC","AUA","AUU"],["K","AAG","AAA"],["L","CUC","CUA","UUG","UUA","CUU","CUG"],["M","AUG"],["N","AAC","AAU"],["P","CCC","CCA","CCU","CCG"],["Q","CAG","CAA"],["R","CGA","CGU","CGC","CGG","AGG","AGA"],["S","UCU","UCA","UCC","UCG","AGU","AGC"],["T","ACU","ACG","ACA","ACC"],["V","GUU","GUA","GUC","GUG"],["W","UGG"],["Y","UAU","UAC"]]

o=[]
db=0


n = n.replace("T", "U")



for i in range(0, int(len(n)/3)):
        db=0
        if i==0 : tri = n[0:3]
        else : tri=n[i*3:(i+1)*3]
        for a in c:
                for b in a:
                        if b == tri :
                                o+=a[0]
                                break
                        
print("".join(o))

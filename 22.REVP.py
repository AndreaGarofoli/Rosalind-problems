""" 
Problem:

A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC. See Figure 2.

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.

"""

from Bio import SeqIO


c=[["A","T"],["T","A"],["C","G"],["G","C"]]

for seq_record in SeqIO.parse("in_22.txt", "fasta"):
        for l in range(4,14,2): 
                for s in range(0,len(seq_record.seq)-l+1): 
                        db=0
                        for o in range(0,int(l/2)): 
                                for cc in range(0,len(c)): 
                                        if seq_record.seq[s+o] == c[cc][0] and seq_record.seq[s+l-o-1] == c[cc][1]: db+=1
                                if db == int(l/2): print(s+1,l)
                               
                        
                

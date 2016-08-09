
"""

Problem:

The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.

"""

print("Write down mRNA sequence")

n = input()


c= [["A","GCU","GCA","GCC","GCG"],["C","UGC","UGU"],["D","GAU","GAC"],["E","GAA","GAG"],["F","UUC","UUU"],["G","GGU","GGG","GGC","GGA"],["H","CAC","CAU"],["I","AUC","AUA","AUU"],["K","AAG","AAA"],["L","CUC","CUA","UUG","UUA","CUU","CUG"],["M","AUG"],["N","AAC","AAU"],["P","CCC","CCA","CCU","CCG"],["Q","CAG","CAA"],["R","CGA","CGU","CGC","CGG","AGG","AGA"],["S","UCU","UCA","UCC","UCG","AGU","AGC"],["T","ACU","ACG","ACA","ACC"],["V","GUU","GUA","GUC","GUG"],["W","UGG"],["Y","UAU","UAC"]]

o=[]

db=0


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

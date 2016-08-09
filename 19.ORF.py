"""

Problem:

Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string implies six total reading frames, or ways in which the same region of DNA can be translated into amino acids: three reading frames result from reading the string itself, whereas three more result from reading its reverse complement.

An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without any other stop codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.

Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.


"""


import re

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


def protx(s):
    pp=[]
    nu=[]
    p = re.compile("AUG")
    for m in p.finditer(s):
            nu.append(int(m.start()))

    for x in nu:
        bc=0
        o=[]
        s1=list(s)
        del s1[0:x]
        s1="".join(s1)
        for i in range(0, int(len(s1)/3)):
            if i==0 : tri = s1[0:3]
            else : tri=s1[i*3:(i+1)*3]
            if tri == "UAG" or tri == "UGA" or tri == "UAA" :
                bc=1

                break
            for a in c:
                for b in a:
                    if b == tri :
                        o+=a[0]
                        break
                                
        if bc == 1 : pp.append("".join(o))
    return(pp)


print("Write down the sequence you want to transcribe")
s = input()




c= [["A","GCU","GCA","GCC","GCG"],["C","UGC","UGU"],["D","GAU","GAC"],
    ["E","GAA","GAG"],["F","UUC","UUU"],["G","GGU","GGG","GGC","GGA"],
    ["H","CAC","CAU"],["I","AUC","AUA","AUU"],["K","AAG","AAA"],
    ["L","CUC","CUA","UUG","UUA","CUU","CUG"],["M","AUG"],["N","AAC","AAU"],
    ["P","CCC","CCA","CCU","CCG"],["Q","CAG","CAA"],
    ["R","CGA","CGU","CGC","CGG","AGG","AGA"],
    ["S","UCU","UCA","UCC","UCG","AGU","AGC"],["T","ACU","ACG","ACA","ACC"],
    ["V","GUU","GUA","GUC","GUG"],["W","UGG"],["Y","UAU","UAC"]]

pr=[]


s = s[::-1]
s = s.replace("T", "a")
s = s.replace("C", "g")
s = s.replace("G", "c")
s = s.replace("A", "u")
s=s.upper()



pr.append(protx(s))

s = s[::-1]
s = s.replace("U", "a")
s = s.replace("C", "g")
s = s.replace("G", "c")
s = s.replace("A", "u")
s=s.upper()


pr.append(protx(s))

pr2 = [ y for x in pr for y in x]


for ss in f7(pr2): print(ss)


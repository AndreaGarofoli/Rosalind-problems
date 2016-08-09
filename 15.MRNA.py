
"""

Problem

For positive integers a and n, a modulo n (written a mod n in shorthand) is the remainder when aa is divided by nn. For example, 29 mod 11= 7 because 29=11×2+7.

Modular arithmetic is the study of addition, subtraction, multiplication, and division with respect to the modulo operation. We say that a and b are congruent modulo n if a mod n = b mod n; in this case, we use the notation a≡ b mod n.

Two useful facts in modular arithmetic are that if a≡ b mod n and c≡ d mod n, then a+c≡ b+d mod n and a×c≡ b×d mod n. To check your understanding of these rules, you may wish to verify these relationships for a=299, b=73, c=10, d=32, and n=11.

As you will see in this exercise, some Rosalind problems will ask for a (very large) integer solution modulo a smaller number to avoid the computational pitfalls that arise with storing such large numbers.

Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)

"""

print("Write down the AA sequence")

n = input()


c= [["A","GCU","GCA","GCC","GCG"],["C","UGC","UGU"],["D","GAU","GAC"],["E","GAA","GAG"],["F","UUC","UUU"],["G","GGU","GGG","GGC","GGA"],["H","CAC","CAU"],["I","AUC","AUA","AUU"],["K","AAG","AAA"],["L","CUC","CUA","UUG","UUA","CUU","CUG"],["M","AUG"],["N","AAC","AAU"],["P","CCC","CCA","CCU","CCG"],["Q","CAG","CAA"],["R","CGA","CGU","CGC","CGG","AGG","AGA"],["S","UCU","UCA","UCC","UCG","AGU","AGC"],["T","ACU","ACG","ACA","ACC"],["V","GUU","GUA","GUC","GUG"],["W","UGG"],["Y","UAU","UAC"]]


num=3

for i in range(len(n)):
        for a in range(len(c)):
                if n[i] == c[a][0]:
                        num=num*(len(c[a])-1)
                
                
print(num % 1000000)

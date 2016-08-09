"""
Problem:

In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string ss is the string s^c formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string ss of length at most 1000 bp.

Return: The reverse complement s^c of s.

"""


print("Write down the sequence you want to use to obtain a complementary strand")

s = input()
s = s[::-1] 

s = s.replace("T", "a")
s = s.replace("C", "g")
s = s.replace("G", "c")
s = s.replace("A", "t")

print(s.upper()) 



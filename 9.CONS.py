"""

Problem

A matrix is a rectangular table of values divided into rows and columns. An m×nm×n matrix has m rows and n columns. Given a matrix A, we write Ai,j to indicate the value found at the intersection of row i and column j.

Say that we have a collection of DNA strings, all having the same length n. Their profile matrix is a 4×n matrix P in which P1,j represents the number of times that 'A' occurs in the jth position of one of the strings, P2,j represents the number of times that C occurs in the jth position, and so on (see below).

A consensus string c is a string of length n formed from our collection by taking the most common symbol at each position; the jth symbol of c therefore corresponds to the symbol having the maximum value in the j-th column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.

					A T C C A G C T
					G G G C A A C T
					A T G G A T C T
DNA Strings			A A G C A A C C
					T T G G A A C T
					A T G C C A T T
					A T G G C A C T
				
				
				A   5 1 0 0 5 5 0 0
Profile			C   0 0 1 4 2 0 6 1
				G   1 1 6 3 0 1 0 0
				T   1 5 0 0 0 1 1 6
				
Consensus			A T G C A A C T


Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

"""


from Bio import SeqIO

nuc = ["A","C","G","T"]
field = []
z = []

s=next(SeqIO.parse("in_9.txt", "fasta"))

l=len(s.seq)

s=SeqIO.parse("in_9.txt", "fasta")


for i in range(0,4):
    field = []
    for j in range(0,l):
        x = 0
        field.append(x)
    z.append(field)


for seq in s:
    nn=0
    for n in seq.seq:
        z[nuc.index(n)][nn]=z[nuc.index(n)][nn]+1
        nn=nn+1


cons = ""

for x in range(0,l):
    n=0
    for y in range(0,4):
        if z[y][x] > n:
            n=z[y][x]
            ch=nuc[y]
    cons+=str(ch)

print(cons)

for i in range(0,4):
    z[i].insert(0,nuc[i])
    z[i][0]+=str(":")

print('\n'.join([''.join(['{:2}'.format(item) for item in row]) 
      for row in z]))


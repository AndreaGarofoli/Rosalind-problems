"""

Problem

To allow for the presence of its varying forms, a protein motif is represented by a shorthand as follows: [XY] means "either X or Y" and {X} means "any amino acid except X." For example, the N-glycosylation motif is written as N{P}[ST]{P}.

You can see the complete description and features of a particular protein by its access ID "uniprot_id" in the UniProt database, by inserting the ID number into

http://www.uniprot.org/uniprot/uniprot_id
Alternatively, you can obtain a protein sequence in FASTA format by following

http://www.uniprot.org/uniprot/uniprot_id.fasta
For example, the data for protein B5ZC00 can be found at http://www.uniprot.org/uniprot/B5ZC00.

Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.


"""

import re
import urllib.request
from Bio import SeqIO



s = open("in_18.txt","r").read().split('\n')

for id in s:
    url = 'http://www.uniprot.org/uniprot/'+id+'.fasta'
    wp = urllib.request.urlopen(url)
    fast = wp.read()
    fast=fast.decode('ascii')
    fast=fast.split("\n")
    del fast[0]
    fast="".join(fast)
    p = re.compile("(?=(N[^P][ST][^P]))")
    nu=[]
    for m in p.finditer(fast):
        nu.append(int(m.start())+1)
    if nu:
        print(id)
        print(" ".join(str(x) for x in nu))




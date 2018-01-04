#!/usr/bin/python

# Converts Genbank to GFF3 suitable for transcriptomics analysis
# Requires biopython, bcbio
# If you want the fasta added, need to include TRUE in the sys args

from Bio import SeqIO
from BCBio import GFF
import sys

try:
   handle = open(sys.argv[1], 'r')
   parameter = sys.argv[3]
   out_handle = open(sys.argv[2], 'w')
except:
   print "Usage: python convertgbktogff3.py infilename outfilename TRUE/FALSE (for writing the sequence fasta in the file)"

print parameter

if parameter == 'TRUE':
     GFF.write(SeqIO.parse(handle, "genbank"), out_handle, include_fasta=True)
else:
     GFF.write(SeqIO.parse(handle, "genbank"), out_handle)

handle.close()
out_handle.close()

 

#!/usr/bin/python

# Converts Genbank to GFF3 suitable for transcriptomics analysis
# Requires biopython, bcbio

from Bio import SeqIO
from BCBio import GFF
import sys

try:
   handle = open(sys.argv[1], 'r')
   out_handle = open(sys.argv[2], 'w')
except:
   print "Usage: python convertgbktogff3.py infilename outfilename"

GFF.write(SeqIO.parse(handle, "genbank"), out_handle)

handle.close()
out_handle.close()

 

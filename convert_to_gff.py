#!/usr/bin/python


from Bio import SeqIO
from BCBio import GFF
import sys

try:
   handle = open(sys.argv[1], 'r')
   outfile = open(sys.argv[1]+".gff", 'w')
except:
   print "Usage: python convert_to_gff.py infile genbank/embl"

if sys.argv[2] == "genbank":
    GFF.write(SeqIO.parse(handle, "genbank"), outfile)
elif sys.argv[2] == "embl":
    GFF.write(SeqIO.parse(handle, "embl"), outfile)
elif sys.argv[2] == "fasta":
    GFF.write(SeqIO.parse(handle, "fasta"), outfile)
else:
    print "Error: Unsupported format, please choose genbank, embl (or fasta)"


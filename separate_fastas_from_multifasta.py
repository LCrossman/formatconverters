#!/usr/bin/python


from Bio import SeqIO
import sys


handle = open(sys.argv[1], 'r')


records = list(SeqIO.parse(handle, "fasta"))

for rec in records:
    outfile = open(rec.id+".fas", "w")
    SeqIO.write(rec, outfile, "fasta")



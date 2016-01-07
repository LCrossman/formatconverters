#Script for converting multigbk to multifasta
#does not use Biopython

gbk_file = raw_input('which genbank input file? ')
fna_file = raw_input('which output filename? ')

file = open(gbk_file, "r")
outfile = open(fna_file, "w")
flag = 0
i = 0

for line in file:
     if line[0:5] == 'LOCUS':
          AC = line.split()[1].strip()
          outfile.write('>'+AC+'\n')
          print "converting new record"
          i = i + 1
     if line[0:6] == 'ORIGIN':
          flag = 1
          continue
     if line[0:2] == '//':
          flag = 0
          continue
     if flag == 1:
          fields = line.split()
          if fields != []:
                 seq = ''.join(fields[1:])
                 outfile.write(seq + '\n')

print "converted %i records"%(i)
file.close()
outfile.close()

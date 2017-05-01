#! /usr/bin/env python3.5

# this program calculates the nucleotide composition for the features in a genome

# load the system module
import sys

# declare the file names
gff_file = 'watermelon.gff'
fsa_file = 'watermelon.fsa'

# open the files for reading
gff_in = open(gff_file, 'r')
fsa_in = open(fsa_file, 'r')

# declare variable that will hold the genome sequence
genome = ''

# initialize a line counter
line_number = 0

# read in the genome file
for line in fsa_in:
    # print(str(line_number) + ": " + line)

    # remove newline's - could also use strip
    line = line.rstrip('\n')

    if line_number > 0:
        genome = genome + line

    # increment line_number
    line_number += 1

# did we get the genome correctly?
# print(len(genome))
    
# close the genome file
fsa_in.close()

cds     = ''
trna    = ''
rrna    = ''
intron  = ''
misc    = ''
repeats = ''

# read in the GFF file
for line in gff_in:

    # remove newline's - could also use strip
    line = line.rstrip('\n')

    types = line.split('; type ')
    other_type = types[len(types)-1]
    # print(other_type)
    
    fields = line.split('\t')
    type  = fields[2]
    start = int(fields[3])
    end   = int(fields[4])
    
    # print(type, "\t", start, "\t", end)

    # extract this feature from the genome
    fragment = genome[start-1:end]

    if type == 'CDS':
        cds += fragment

    if type == 'intron':
        intron += fragment

    if type == 'misc_feature':
        misc += fragment

    if type == 'repeat_region':
        repeats += fragment

    if type == 'rRNA':
        rrna += fragment

    if type == 'tRNA':
        trna += fragment

# print the output
print(cds.count('G'))
print(cds.count('C'))
    

# close the GFF file
gff_in.close()

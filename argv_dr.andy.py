#! /usr/bin/env python3.5

import sys

## for argument in sys.argv:
##     print(argument)

## sys.exit()

usage = sys.argv[0] + ": genome.fasta features.gff"

if len(sys.argv) < 3:
    print(usage)
    sys.exit("\nThis script requires both a FASTA file and a GFF file\n")

genome = sys.argv[1]
gff    = sys.argv[2]

print(gff + "\n" + genome)

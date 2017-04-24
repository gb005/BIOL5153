
# coding: utf-8

# In[442]:

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
genome_length = len(genome)
#print(genome_length)

# close the genome file
#fsa_in.close()

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
        
    if type == 'rRNA':
        rrna += fragment  
        
    if type == 'repeat_region':
        repeats += fragment
    
    if type == 'tRNA':
        trna += fragment
        
# print the output
# print(cds.count('G'))
# print(cds.count('C'))

length_cds = len(cds)
# print(length_cds)
length_intron = len(intron)
#print(length_intron)
length_misc = len(misc)
#print(length_misc)
length_rRNA = len(rrna)
#print(length_rRNA)
length_repeats = len(repeats)
#print(length_repeats)
length_trna = len(trna)
#print(length_trna)

#percentage of genome covered by exon
percent_exon = (length_cds/genome_length)*100
# print('(',round(percent_exon,2),"%",')')
GC_cds = (((cds.count('G') + cds.count('C'))/length_cds)*100)
print("exon             ", length_cds ,"  ", '(',round(percent_exon,2),"%",')', "  ", round(GC_cds,2))

# percentage of genome covered by intron
percent_intron = (length_intron/genome_length)*100
GC_intron = (((intron.count('G') + intron.count('C'))/length_intron)*100)
print("intron           ", length_intron ,"  ",'(',round(percent_intron,2),"%",')', "  ", round(GC_intron,2))

# percentage of genome covered by misc_feature
percent_misc = (length_misc/genome_length)*100
GC_misc = (((misc.count('G') + misc.count('C'))/length_misc)*100)
print("misc_feature     ", length_misc , "  ",'(',round(percent_misc,2),"%",')', "   ",round(GC_misc,2))

# percentage of genome covered by rrna
percent_rrna = (length_rRNA/genome_length)*100
GC_rrna = (((rrna.count('G') + rrna.count('C'))/length_rRNA)*100)
print("rRNA             ", length_rRNA , "  ",'(',round(percent_rrna,2),"%",')', "   ", round(GC_rrna,2))

# percentage of genome covered by repat_region
percent_repeats = (length_repeats/genome_length)*100 
GC_repeats = (((repeats.count('G') + repeats.count('C'))/length_repeats)*100)
print("repeat_region    ", length_repeats , "  ",'(',round(percent_repeats,2),"%",')', "  ", round(GC_repeats,2))

# percentage of genome covered by repat_region
percent_trna = (length_trna/genome_length)*100 
GC_trna = (((trna.count('G') + trna.count('C'))/length_trna)*100)
print("tRNA             ", length_trna , "  ",'(',round(percent_trna,2),"%",')', "   ", round(GC_trna,2))


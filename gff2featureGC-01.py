
# coding: utf-8

# In[444]:

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

# output after running the codes are shown below:
# exon              32442    ( 8.55 % )    43.12
# intron            32476    ( 8.56 % )    51.37
# misc_feature      24282    ( 6.4 % )     37.39
# rRNA              5148    ( 1.36 % )     52.45
# repeat_region     14572    ( 3.84 % )    45.66
# tRNA              1358    ( 0.36 % )     50.22


# coding: utf-8

# In[39]:

# this program calculates the nucleotide composition for the features in a genome

# load the system module
import sys
andy = 42
print("Main-1:", andy)

# a function to clean up a DNA sequence
def clean_seq(input_seq):
    clean = input_seq.upper()
    clean = clean.replace('N', '')
    return clean


def nuc_freq(sequence, base, sig_digs=2):
    # Calculate the length of the sequence
    length = len(sequence)
    
    # count the number of this nucleotide
    count_of_base = count(base)

    # Calculate the base frequencey
    feq_of_base = count_of_base/length
    
    # return the frequency and the length
    return (length, round(freq_of_base, sig_digs))

# key = feature type, value = concatenation of all sequences of that 
feature_sequences = {}

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
print("total genomic length of 'genome' variable is: ", len(genome))

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

    # extract and clean the sequence of this feature from the genome
    fragment = genome[start-1:end]
    fragment = clean_seq(fragment)
    
    if type in feature_sequences:
        feature_sequences[type] += fragment
    else:
        feature_sequences[type] = fragment
    # print(clean_seq)

    

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


        
# close the GFF file
gff_in.close()



for feature, sequence in feature_sequences.items():
    print(feature + "\t" + str(len(sequence)))
    #print(len(sequence))
    
    
#for feature_type in list_of _features:
    # loop over the 4 nucleotides
    # for nucleotide in [A, C, G, T]:
    
        # Calculate the nucleotide compostion for each feature
        #(feature_length, feature_comp) = nuc_freq(feature_type, base=nucleotide, sig_digs =2)
        #print('cds\t' + str(feature_length) + "\t" +str(feature_comp)+ "A")


# print the output
#print(cds.count('G'))
#print(cds.count('C'))
    

# close the GFF file
#gff_in.close()


# In[ ]:



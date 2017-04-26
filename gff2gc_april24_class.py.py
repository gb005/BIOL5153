
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




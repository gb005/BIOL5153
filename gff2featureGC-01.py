
#! /home/gb005/anaconda3/bin/python3.6
# this program calculates the nucleotide composition for the features in a genome

# load the system module
import sys
import collections

andy = 42
#print("Main-1:", andy)

# a function to clean up a DNA sequence
def clean_seq(input_seq):
    clean = input_seq.upper()
    clean = clean.replace('N', '')
    return clean


def nuc_freq(sequence, base1, base2,sig_digs=2):
    # Calculate the length of the sequence
    length = len(sequence)
    
    # genome covered with each feature class
    genome_cover=(len(sequence)/len(genome))*100
    
    # count the number of this nucleotide
    base_1_count = sequence.count(base1)
    
    base_2_count = sequence.count(base2)

    # Calculate the GC content
    gc_content = ((base_1_count+base_2_count)/length)*100
    # print(gc_content)
    #feq_of_base = count_of_base/length
    
    # return the frequency and the length
    return (length, genome_cover, round(gc_content, sig_digs))

# function to get reverse complement sequences
def reverse(dna_seq):
    complement0 = (dna_seq.replace("A", "t"))
    complement1 = (complement0.replace("C", "g"))
    complement2 = (complement1.replace("T", "a"))
    complement3 = (complement2.replace("G", "c"))
    return (complement3.upper())

usage = sys.argv[0] + ": watermelon.fsa watermelon.gff"

if len(sys.argv) < 3:
    print(usage)
    sys.exit

# read above arguments
gff = sys.argv[1]
fsa = sys.argv[2]
#print(genome)

gff_file = "watermelon.gff"
fsa_file = "watermelon.fsa"

#open the files
gff_in = open(gff_file, 'r')
fsa_in = open(fsa_file, 'r')

# Creating dictionary
# key = feature type, value = concatenation of all sequences of that type-not useful for anything other than calculating AT/GC content

feature_sequences={}

#key exon, value sequence
exon_sequences={}

# key is gene and value is concatenation of all exon sequences in a gene
gene_sequences={}

#declare a variable
genome = ''

line_number = 0

for line in fsa_in:
    # print(str(line_number) + ": " + line)
    
    line = line.rstrip('\n')
    #print(str(line_number) + ": " + line)
    if line_number > 0:
        genome+=line
        
    line_number+=1
    
#check if we get genome correctly
# print(len(genome))

#close the fsa file
fsa_in.close()

cds = ''
trna = ''
rrna = ''
intron = ''
misc = ''
repeats = ''

for line in gff_in:
    line = line.rstrip('\n')
    types = line.split('type')
    other_type = types[len(types)-1]
    #print(line)
    #print(types)
    #print(other_type)
    
    fields = line.split('\t')
    #print(fields)
    type = fields[2]
    #print(type)
    strand = fields[6]
    #print(strand)
    
    start = int(fields[3])
    #print(start)
    
    end = int(fields[4])
    #print(end)
    
    # print(type, "\t",start, "\t",end)
    
    
    # now extract features from the genome
    fragment = genome[start-1:end]
    #print(fragment)
    fragment = clean_seq(fragment)
    #print(fragment)
    
    if type in feature_sequences:
        feature_sequences[type] += fragment
    else:
        feature_sequences[type]=fragment
        
    if type == 'CDS':
        gene_feature = fields[8]
        gene1 = gene_feature.split(':')
        gene = gene1[0]
        gene_seq = genome[start-1:end]
        #print(gene)
        #print(gene_seq)
        
        
        if strand == '-':
            complement_sequence = reverse(gene_seq)
            exon_sequences[gene] = complement_sequence
        else:
            exon_sequences[gene] = gene_seq
    # print(exon_sequences)
    # print(gene)
    
#close tthe file
gff_in.close()

# now need to order the exon sequences
ordered_exons_sequences = collections.OrderedDict(sorted(exon_sequences.items()))

#for exon, sequence in ordered_exons_sequences.items():
    #print(">", exon, "\n", sequence)
    # this prints the exons along with the sequences in fasta fmt
    
for feature, sequence in feature_sequences.items():
    (feature_length, cover, feature_comp) = nuc_freq(sequence, base1='C',base2='G',sig_digs=2)
    
    print(feature, "\t" , str(len(sequence)), str(round(cover, 1)) + "%", "\t",str(feature_comp)+ "%")
    
    #print(feature, "\t", str(round(cover, 1)) +"%") # check
    #feature_length = nuc_freq(sequence, base1, base2, sigs_digs=2) #check
    #print(feature_length) #check
    #print(feature + "          \t" + str(len(sequence))) #check
   


# In[ ]:




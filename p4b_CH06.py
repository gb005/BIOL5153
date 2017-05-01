
# coding: utf-8

# In[2]:

# Conditions, True and False
print(3 == 5)
print(3 > 5)
print(3 <=5)
print(len("ATGC") > 5)
print("GAATTC".count("T") > 1)
print("ATGCTT".startswith("ATG"))
print("ATGCTT".endswith("TTT"))
print("ATGCTT".isupper())
print("ATGCTT".islower())
print("V" in ["V", "W", "L"])


# In[4]:

# if statements
expression_level = 125
if expression_level > 100:
    print("gene is highly expressed")


# In[16]:

# printing name of genes start with 'a'
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for accession in accs:
    if accession.startswith('a'):
        print(accession)
print("*************")        
genotype = ['f_apple', 'f_pear', 'v_spinach', 'v_kale']
for crops in genotype:
    if crops.startswith('v'):
        print(crops)


# In[20]:

# else statements
expression_level = 28
if expression_level > 100:
    print("gene is highly expressed")
else:
    print("gene is lowly expressed")


# In[24]:

file1 = open("one.txt", "w")
file2 = open("two.txt", "w")
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for accession in accs:
    if accession.startswith('a'):
        file1.write(accession + "\n")
    else:
        file2.write(accession + "\n")


# In[26]:

for accession in accs:
    if accession.startswith('a'):
        file1.write(accession + "\n")
    elif accession.startswith('b'):
        file2.write(accession + "\n")
    elif accession.startswith('c'):
        file3.write(accession + "\n")
    elif accession.startswith('d'):
        file4.write(accession + "\n")
    else:
        accession.startswith('e'):
        file5.write(accession + "\n")


# In[34]:

# while loops
count = 0
while count<8:
    print(count)
    count = count + 1


# In[37]:

# combining formats usinh if
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for accession in accs:
    if accession.startswith('a'):
        if accession.endswith('3'):
            print(accession)


# In[39]:

# starts with either a or b and ends with 4
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for acc in accs:
    if (acc.startswith('a') or acc.startswith('b')) and acc.endswith('4'):
        print(acc)


# In[41]:

# starts with 'a' and don't end with 6
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for acc in accs:
    if acc.startswith('a') and not acc.endswith('6'):
        print(acc)


# In[45]:

# Writing true/false functions
# dna = "ATTATCTACTA"
def is_at_rich(dna):
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count) / length
    if at_content > 0.65:
        return True
    else:
        return False


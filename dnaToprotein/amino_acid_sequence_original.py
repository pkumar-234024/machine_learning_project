# Python program to convert DNA to PROTEIN


# FUNCTIO FOR CONVERT DNA TO PROTEIN
#-----------------------------------------------------------------#
def translate(seq): 

	table = { 
		'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
		'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
		'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
		'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',				 
		'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
		'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
		'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
		'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
		'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
		'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
		'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
		'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
		'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
		'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
		'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 
		'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W', 
	} 
	protein ="" 
	if len(seq)%3 == 0: 
		for i in range(0, len(seq), 3): 
			codon = seq[i:i + 3] 
			protein+= table[codon] 
	return protein 
#-----------------------------------------------------------------#

#FUNCTIO FOR READ THE INPUT FILE AND
#RREMOVE NEW LINE AND ANY SPECIFIC SYMBOL
#RETURN THE FINALIZE SEQUENCE OF DNA
#-----------------------------------------------------------------#
def read_seq(inputfile): 
	with open(inputfile, "r") as f: 
		seq = f.read() 
	seq = seq.replace("\n", "") 
	seq = seq.replace("\r", "") 
	return seq 
#-----------------------------------------------------------------#

#TAKE INPUT IN A TXT FORMAT
#FIND THE LENGTH OF THE FINALIZE DNA SEQUENCE
#-----------------------------------------------------------------#

input_file = "DNA_sequence_original.txt"
dna = read_seq(input_file) 
l = len(dna)
index = l%3
#-----------------------------------------------------------------#


#PRINT THE CONVERTED PROTEIN SEQUNCE FROM DNA
#-----------------------------------------------------------------#

p = translate(dna[:l-index])
print(p)
#-----------------------------------------------------------------#

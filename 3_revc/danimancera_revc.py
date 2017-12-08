nucleotides = {'A':'T','C':'G','T':'A','G':'C'}
#counts = {i:0 for i in nucleotides}
strain = ''

with open('./rosalind_revc.txt') as fp:
    for line in fp:
        for nucleotide in line:
            if nucleotide in nucleotides:
                strain += nucleotides[nucleotide]
print strain[::-1]
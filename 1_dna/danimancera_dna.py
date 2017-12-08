nucleotides = {'A','C','T','G'}
counts = {i:0 for i in nucleotides}
with open('./rosalind_dna.txt') as fp:
    for line in fp:
        for nucleotide in line:
            if nucleotide in counts:
                counts[nucleotide]+=1

print counts
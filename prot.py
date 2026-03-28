# Rosalind PROT: Translating RNA into Protein
# Professional, efficient, no extra libraries needed (fast for 10kbp RNA)

codon_table = {
    'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
    'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',
    'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
    'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
    'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
    'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
    'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
    'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
    'UAC':'Y', 'UAU':'Y', 'UAA':'*', 'UAG':'*',
    'UGC':'C', 'UGU':'C', 'UGA':'*', 'UGG':'W',
}

def translate_rna_to_protein(rna_str):
    """Efficient function: RNA ko protein mein translate karta hai"""
    protein = ''
    # Har 3 letters (codon) ko check karo
    for i in range(0, len(rna_str) - 2, 3):
        codon = rna_str[i:i+3]
        amino_acid = codon_table.get(codon, '*')  # Agar codon galat ho to stop
        if amino_acid == '*':  # Stop codon aaya to ruk jao
            break
        protein += amino_acid
    return protein

# Main part: Dataset file se read karo
with open('rosalind_prot.txt', 'r') as file:
    rna_input = file.read().strip()  # Extra spaces hatao

# Function call aur output
result_protein = translate_rna_to_protein(rna_input)
print(result_protein)

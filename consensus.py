def get_consensus_and_profile(fasta_data):
    """
    Core function jo FASTA format data ko parse karke 
    Consensus aur Profile Matrix return karta hai.
    """
    sequences = []
    # Data ko '>' symbol se split karna
    blocks = fasta_data.strip().split('>')
    
    # --- PART 1: Safe Data Parsing ---
    for block in blocks:
        if not block.strip():
            continue
        
        # .splitlines() \n aur \r dono ko safely handle karta hai
        lines = block.splitlines()
        
        # Label (lines[0]) ko ignore karein aur sequence ko join karein
        # .strip() ensure karta hai ki koi invisible space na bache
        dna = "".join(line.strip() for line in lines[1:])
        if dna:
            sequences.append(dna)
            
    if not sequences:
        return "", {}

    n = len(sequences[0])
    
    # --- PART 2: Profile Matrix Population ---
    # Dictionary of lists se O(1) update speed milti hai
    profile = {base: [0] * n for base in ['A', 'C', 'G', 'T']}
    
    for seq in sequences:
        for i, base in enumerate(seq):
            if base in profile:  # Safe check against wrong characters
                profile[base][i] += 1
                
    # --- PART 3: Consensus String Generation ---
    consensus = []
    bases = ['A', 'C', 'G', 'T']
    
    for i in range(n):
        max_count = -1
        best_base = 'A'
        
        for base in bases:
            if profile[base][i] > max_count:
                max_count = profile[base][i]
                best_base = base
                
        consensus.append(best_base)
        
    return "".join(consensus), profile


def main():
    # --- Input Data Setup ---
    # Aap dataset ko is string ke beech mein paste kar sakte hain
    fasta_data = """>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT"""

    # HINT: Agar File se read karna ho, toh in 4 lines ke aage se '#' hata dein:
    # try:
    #     with open("rosalind_cons.txt", "r") as file:
    #         fasta_data = file.read()
    # except FileNotFoundError:
    #     print("Dataset file nahi mili!")
    #     return

    # --- Processing ---
    consensus_str, profile_matrix = get_consensus_and_profile(fasta_data)
    
    if not consensus_str:
        print("Error: Dataset khali hai ya galat format mein hai.")
        return

    # --- Printing in Exact Rosalind Format ---
    print(consensus_str)
    for base in ['A', 'C', 'G', 'T']:
        # Counts ko string banakar space se join karna
        counts_line = " ".join(map(str, profile_matrix[base]))
        print(f"{base}: {counts_line}")


# Standard Python boilerplate execution ke liye
if __name__ == '__main__':
    main()
with open('rosalind_revc.txt','r')as file:
    s=file.read().strip()
    complement={'A':'T','T':'A','C':'G','G':'C'}
    reverse=''.join(complement[base] for base in reversed(s))
    print(reverse)

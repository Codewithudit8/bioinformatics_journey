with open('rosalind_dna (1).txt','r')as f:
    dna=f.read().strip()
    A=dna.count('A')
    C=dna.count('C')
    G=dna.count('G')
    T=dna.count('T')
    print(A,C,G,T)

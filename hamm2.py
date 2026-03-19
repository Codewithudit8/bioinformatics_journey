with open('rosalind_hamm.txt','r') as f:
    s1=f.readline().strip()
    s2=f.readline().strip()
    print(sum(1 for a,b in zip(s1,s2) if a!=b))
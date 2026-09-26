# Input:  A DNA string Genome
# Output: A list containing all integers i minimizing Skew(Prefix_i(Text)) over all values of i (from 0 to |Genome|)
def SkewArray(Genome):
    n = len(Genome)
    skew=[0]
    for i in range(n):
        if Genome[i]=="A" or Genome[i]=="T":
            skew.append(skew[i])
        elif Genome[i]=="G":
            skew.append(skew[i]+1)
        elif Genome[i]=="C":
            skew.append(skew[i]-1)
    return skew
def MinimumSkew(Genome):
    skew=SkewArray(Genome)
    position=[]
    n=len(skew)
    smallest=min(skew)
    for i in range(1,n):
        if skew[i]==smallest:
            position.append(i)
    return position
dynamic_genome=input().strip()
result=MinimumSkew(dynamic_genome)
print(*result)

# Input:  A String Genome
# Output: The skew array of Genome as a list.
def SkewArray(Genome):
    n=len(Genome)
    arr=[0]*(n+1)
    arr=[0]       # Step 2: Loop chala kar sequence ke har nucleotide ko check karein
    for i in range(n):
        if Genome[i] == "A" or Genome[i] == "T":
            # A ya T par skew same rehta hai, pichli value ko append karein
            arr.append(arr[i])
        elif Genome[i] == "G":
            # G par skew +1 badhta hai
            arr.append(arr[i] + 1)
        elif Genome[i] == "C":
            # C par skew -1 ghat-ta hai
            arr.append(arr[i] - 1)
            
    # Step 3: Loop khatam hone ke baad poora array return karein, na ki sirf ek value
    return arr

# Function ko call karein aur result print karein
result = SkewArray("ATCGTCGA")
print(result)

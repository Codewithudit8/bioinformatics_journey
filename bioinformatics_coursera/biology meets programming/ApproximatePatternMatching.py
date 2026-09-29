# Input:  Strings Pattern and Text along with an integer d
# Output: A list containing all starting positions where Pattern appears
def HammingDistance(p, q):
    # Yeh function sirf do strings ke beech mismatches ginta hai
    count = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count

def ApproximatePatternMatching(Text, Pattern, d):
    positions = []
    k = len(Pattern)
    n = len(Text)
    
    # Text par standard sliding window chalayenge
    for i in range(n - k + 1):
        # Current window ka substring nikalenge
        current_kmer = Text[i:i+k]
        
        # Helper function se check karenge ki mismatches 'd' limit ke andar hain ya nahi
        if HammingDistance(Pattern, current_kmer) <= d: # now work flow will go to the first function and after returning count it will comeback here for compare.
            positions.append(i)
            
    return positions

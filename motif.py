
# Step 1: Dataset file se read karo (Rosalind format)
with open('rosalind_subs.txt', 'r') as file:
    s = file.readline().strip()   # pehli line = badi DNA string
    t = file.readline().strip()   # doosri line = motif

# Step 2: Positions store karne ke liye list
positions = []

# Step 3: Efficient loop - har possible starting point check karo
for i in range(len(s) - len(t) + 1):
    if s[i:i + len(t)] == t:      # slice se substring compare
        positions.append(str(i + 1))  # 1-based position
print(' '.join(positions))
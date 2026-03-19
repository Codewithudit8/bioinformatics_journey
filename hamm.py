# hamm.py
# Rosalind HAMM - Counting Point Mutations
# VS Code mein run karne ke liye: python hamm.py

# Step 1: File se data read karo (beginner ke liye simple way)
with open('rosalind_hamm.txt', 'r') as file:   # 'r' = read mode
    s = file.readline().strip()   # pehli line, extra spaces hatao
    t = file.readline().strip()   # dusri line

# Step 2: Counter initialize karo (shuru mein 0)
count = 0

# Step 3: Loop chalao har character pe (ye sabse basic algorithm hai)
for i in range(len(s)):           # range(len(s)) = 0 se length-1 tak
    if s[i] != t[i]:              # agar dono letters alag hain
        count = count + 1         # count badhao

# Step 4: Answer print karo
print(count)
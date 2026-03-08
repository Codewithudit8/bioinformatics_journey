quizess,revision done biology time: 1 h 
python village ini6 problem learn and code time :2 h 
debuging and note making take 1 h 
learn new function today[ini6.py](https://github.com/user-attachments/files/25822047/ini6.py)
# INI6: Dictionaries - Rosalind Dataset Version
# rosalind_ini6.txt file se padhega

# Step 1: Dataset file se input padho
with open('rosalind_ini6 (1).txt', 'r') as f:
    s = f.read().strip()

# Step 2: Words mein split karo
words = s.split()

# Step 3: Dictionary banao count ke liye
count = {}

# Step 4: Har word ka count badhao (clean way)
for word in words:
    count[word] = count.get(word, 0) + 1

# Step 5: Output print karo (kisi bhi order mein)
for word in count:
    print(word, count[word])

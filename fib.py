
# Step 1: Dataset file se n aur k padho
with open('rosalind_fib.txt', 'r') as file:
    line = file.read().strip()          # poori line padh lo
    n, k = map(int, line.split())       # string ko do integers mein badlo

# Step 2: Base cases handle karo
if n == 1 or n == 2:
    result = 1
else:
    # Step 3: Iterative loop (pehle 2 months se start)
    a = 1          # month 1
    b = 1          # month 2
    for month in range(3, n + 1):      # 3 se n tak loop
        c = b + k * a                  # naya formula: previous + k*old
        a = b                          # shift karo aage
        b = c                          # naya b banao
    
    result = b

# Step 4: Final answer
print(result)
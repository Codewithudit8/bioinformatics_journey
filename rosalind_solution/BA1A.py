with open('rosalind_ba1a (1).txt','r')as f :
    data=f.read().strip().splitlines()
    text=data[0].strip()
    pattern=data[1].strip()
def pattern_count(text,pattern):
    count=0
    for i in range(len(text)-len(pattern)+1):
      if text[i:i+len(pattern)] == pattern: #in slicing last value is excluded so +1
       count=count+1
    return count 
print(pattern_count(text,pattern))

   



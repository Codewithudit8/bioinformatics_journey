with open("rosalind_ba1c (2).txt","r")as f:
    text=f.read().strip()
    complement={"A":"T","C":"G","G":"C","T":"A"}
    complement_list=[]
    for base in reversed(text):
        complement_list.append(complement[base])
    reverse="".join(complement_list)
    print(reverse)
        

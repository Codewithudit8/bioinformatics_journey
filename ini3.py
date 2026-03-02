with open('rosalind_ini3.txt','r') as file:   # ye line rosalind main diya gay dataset ka  name padehega ye memory leak se bachata hai
    lines = file.readlines()   # ye file se line read karlega
    s=lines[0].strip()   # yahan string create horaha hai jahan pehle bale main character save hoga and strip command se hidden space at end dur hojaega
    a,b,c,d=map(int,lines[1].split()) # ye abcd 4 number ko integer maain comvert karega joki string 1 main store and and split () enko separate karke store kardega
    w1=s[a:b+1]
    w2=s[c:d+1]
    print(w1,w2)

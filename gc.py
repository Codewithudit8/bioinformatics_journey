def find_max_gc_content(file_path):
    
    with open(file_path, 'r') as file:
        data = file.read().strip()  # saari file ek string mein
    
    
    records = data.split('>')[1:]
    
    max_gc = -1.0          
    max_id = ''           
    
    for record in records:
        
        parts = record.split('\n', 1)     
        seq_id = parts[0].strip()          
        
        
        if len(parts) > 1:
            seq = parts[1].replace('\n', '').strip()
        else:
            seq = ''
        
        
        gc_count = seq.count('G') + seq.count('C')
        length = len(seq)
        if length == 0:
            continue
        gc_percent = (gc_count / length) * 100
        
       
        if gc_percent > max_gc:
            max_gc = gc_percent
            max_id = seq_id
    
  
    print(max_id)
    print(f"{max_gc:.6f}")   # 6 decimal tak (sample jaise)
find_max_gc_content('rosalind_gc.txt')
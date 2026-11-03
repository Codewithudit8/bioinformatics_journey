   GNU nano 8.7.1           countto_1100.py
one=0b1
two=0b10
three=0b11
four=0b100
five=0b101
six=0b110
seven=0b111
eight=0b1000
nine=0b1001
ten=0b1010
eleven=0b1011
twelve=0b1100
print (one,two,three,four,five,six,seven,eight,nine,ten,eleven>
print ("The bin() function")
print (bin(1))
print (bin(2))
for i in range(1,6):
  print (bin(i))
result=[bin(i) for i in range(1,11)]
print ('\n'.join(result))
print ("int() second parameter")
print (int("5"))
print (int("110",2))
print (int("11001001",2))
print (bin(201))
print (int("11001001",8))
print ("slight to the left slide to the right")
shift_right = 0b1100
shift_left = 0b001
r=shift_right >> 2
l=shift_left << 1

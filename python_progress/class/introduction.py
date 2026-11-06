a = 0b11101110
mask=0b11111111
result=a ^ mask
print (f'{a} xor {mask} is : ',bin(result))
print (a,mask,result)
print ("slip and slide")
def flip_bit(number,n):
  mask=0b1
  shift=mask << n-1
  result=number ^ shift
  print (f' xor of {bin(number)} and {bin(shift)} at {n} positi>
  return bin(result)
print (flip_bit(5,2))
print ("class")
class Animal():
  def __init__(self,name):
    pass
    self.name=name

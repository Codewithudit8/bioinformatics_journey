result1=0b1110 ^ 0b101
print (bin(result1))
print (result1)
print (~1)
print (~10)
print (~11)
print (~23)

def check_bit4(input):
  mask=0b1000
  if input & mask == 8:
    print ("ON")
  else:
    print ("OFF")
  return "ok"
check_bit4(0b11000)
def check(input):
  mask=0b1000
  if input & mask > 0:
    return "on"
  else:
    return "off"
print (check(0b10000))
print ("turn it on")
def turn_on(input):
  mask=0b100
  result=input | mask
  print (result)
  return bin(result)
print(turn_on(0b10111011))

def digit_sum(n):
  total = 0
  string_n = str(n)
  for char in string_n:
    total += int(char)
  return total

#Alternate Solution:

def digit_sum(n):
 total = 0
 while n > 0:
   total += n % 10
digit_sum(12345)

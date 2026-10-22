def median(x):
  x=sorted(x)
  n=len(x)
  if n%2 == 0:
    m=int(n/2)
    result=(x[m]+x[m-1])/2.0
  else:
    m=int(n/2)
    result=x[m]
  return result
print (median([2,1,3,4,5]))

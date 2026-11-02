movies = {
  "Monty Python and the Holy Grail": "Great",
  "Monty Python's Life of Brian": "Good",
  "Monty Python's Meaning of Life": "Okay"
}
print (movies.items())
for key,value in  movies.items():
  print (f"key :{key},value : {value}")
print ("key value separate ")
print ("key :",list(movies.keys()))
print ("values : ",list(movies.values()))
print ("")
print ("comprehending comprehensions")
list1=list(range(1,16))
three_to_five=[x for x in list1 if x%3 ==0 or x%5 ==0]
print (three_to_five)
three_and_fives=[x for x in range(1,16) if x %3 ==0 or x %5==0]
print (three_and_fives)
print ("list slicing : ->")
python= "giantpython"
start,end,stride=5,11,1
print (python[start:end:stride])
print ("lambda expressions -->")
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message =''.join(filter(lambda x : x !='X',garbled))
print (message)
print (garbled.replace("X",''))
print (" introduction to bitwise operator ")
print (0b1,)
print (0b1+0b11)
print (0b100*0b100)

to_21 = list(range(1, 22))

odds = list(to_21[::2])

middle_third = list(to_21[7:14])
print(to_21,odds,middle_third)
my_list=list(range(16))
print (list(filter(lambda x : x%3 == 0,my_list)))
print ("lambda syntax")
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print (list(filter(lambda x: x == "Python", languages)))
print ("try It")
squares=[x ** 2 for x in range(1,11)]
answer=[x ** 2 for x in squares if x ** 2 in range(30,71)]
print (answer)
print (list(filter(lambda x :  x >= 30 and x <=70,squares)))


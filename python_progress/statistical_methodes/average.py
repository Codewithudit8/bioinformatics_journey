## printing the average of the marks of students
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
def grade_sum(grades):
  total=0
  for item in grades:
     total+=item
  return total
def grades_average(grades_input):
  total=grade_sum(grades_input)
  num=len(grades_input)
  avg=total/num
  return avg
print (grades_average(grades))


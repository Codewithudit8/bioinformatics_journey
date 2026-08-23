problem: using object oriented prograaming concept printing name and subjects of students
## abstraction concept: printing status of a car after confirming cluge,gear and  accelaraotr, is True 
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for i in self.marks:
            sum=sum+i  
        print(self.name,"your average score is : ",sum/3)
s1=Student("udit",[99,98,97]) 
s1.get_avg()
      
class Car:
    def __init__(self):
        self.cluge= True
        self.acc= True
        print("car has been started")
    def get_start(self):
        self.cluge=True
        self.acc=True
        print("cluge is pressed")
        print("gear is locked")
car1=Car()
car1.get_start()

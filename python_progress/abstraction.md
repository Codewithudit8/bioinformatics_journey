## abstraction,encapsulation in python
solved 2 problem

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
class Person:
    name="anonymous"
    def change(self,name):
        self.__class__.name="unit"
        self.name = name
p1=Person()
p1.change("udit ")
print(p1.name)
print(Person.name)
## 2nd program 
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.real=img
    def show(self):
        print(self.real,"i+",self.img,"j")
num1=Complex(1,3)
num1.show()

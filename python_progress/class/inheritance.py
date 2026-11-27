class  Shape(object):
  " makes shapes "
  def __init__(self,number_of_slides):
    self.number_of_slides=number_of_slides
  def Triangle(Shape):
    "having three sides"
  def __init__(self,slide1,slide2,slide3):
    self.slide1=slide1
    self.slide2=slide2
    self.slide3=slide3
class Employee(object):
  " it sote the details of employee "
  def __init__(self,employee_name):
    self.employee_name=employee_name
  def calculate_wage(self,hours):
    self.hours=hours
    return hours * 20.00
class PartTimeEmployee(Employee):
  def calculate_wage(self,hours):
    self.hours=hours
    return hours * 12

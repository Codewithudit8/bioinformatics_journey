print ("class scope")
class Animal(object):
  "make cute animals "
  is_alive=True
  def __init__(self,name,age):
    self.name=name
    self.age=age
jaffery=Animal("zebra",10)
prakash=Animal("dog",5)
dr_suresh=Animal("cat",10)
print (jaffery.name,jaffery.age,jaffery.is_alive)
print (prakash.name,prakash.age,jaffery.is_alive)
print (dr_suresh.name,dr_suresh.age,jaffery.is_alive)
print ("A methodical Approach")
class Animal_1(object):
  is_alive=True
  health='they have good health'
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def description(self):
    print (self.name)
    print (self.age)
    print (hippo.health)
zebra=Animal_1("titu",11)
hippo=Animal_1("sino",12)
zebra.description()
hippo.description()
print ('they are multiplying')
print (' it is not all anmilas and fruit')
class Shopping_cart(object):
    """ creating shopping cart object for user of our fine websites"""
  def __init__(self,item,price,quantity,discount):
    self.item=item
    self.price=price
    self.quantity=quantity
    self.discount=discount
  def add_item():
    print (" sarve bhawantu sukhinaha")
my_cart=Shopping_cart("biscuit",30,2,0)
my_cart2=Shopping_cart("icecream",50,3,10)
print (my_cart.item,my_cart.price,my_cart.quantity,my_cart.discount)
print (my_cart2.item,my_cart2.price,my_cart2.quantity,my_cart2.discount)

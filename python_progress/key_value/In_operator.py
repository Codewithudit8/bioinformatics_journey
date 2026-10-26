inventory = {
    "Laptop": 12,
    "Smartphone": 45,
    "Headphones": 0,
    "Smartwatch": 18,
    "Tablet": 0
}
def stocks(reports):
  for i in reports.keys():
    print (f"the list of items are : {i}")
  total=sum(reports.values())
  print (f"the  sum of items  required {total}")
  for product,stock in reports.items():
    print(f"the product and items are {product} ,{stock}")
  for product,stock in reports.items():
    if stock==0:
      print(f"{product} need restocking")
stocks(inventory)

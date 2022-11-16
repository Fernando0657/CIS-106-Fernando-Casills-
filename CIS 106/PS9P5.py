def comptotal(qty,price):
  
  return total







qty = float(input("Enter quantity of item "))
price = float(input("Enter price per unit "))
total = (qty * price)
tax =  0.07 / total * 100
print("Your total is $ ", total)
print("Tax cost is $ ", tax)

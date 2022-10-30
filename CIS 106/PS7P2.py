def comptotal(qty,price):
  total = float(qty) * float(price)
  if total > 10000.00:
    total = total * 0.90 
  else: 
    total = total 

  return total 

qty = float(input("Enter the quantity ")) 
price = float(input("Enter price "))

total = comptotal(qty,price)

print("This is total $ ", total)
print("This is the quantity " + str(qty))
print("Price per item $ ", price)
  
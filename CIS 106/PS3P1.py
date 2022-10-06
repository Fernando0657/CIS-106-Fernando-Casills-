item = input("Please enter item (A or B)")
qty = float(input("Enter qty ordered"))

if item=="A":
  up = 10.00 

else: 
  up = 20.00 
  
extprice = qty * up 

print( "Quantity ordered ", qty)
print("Unit price $" , up)
print("Extended price $" , extprice)


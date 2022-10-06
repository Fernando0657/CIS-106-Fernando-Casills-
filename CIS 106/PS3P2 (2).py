booksordered = float(input("Enter how many books you ordered"))
costper = float(input("Enter the cost per book"))

total = booksordered * costper


if total<50:
  up = 0
  
else: 
  up = 25

shipping = up + total

print("This is your order total", total)
print("This is your shipping cost", shipping) 


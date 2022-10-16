appliance = input("Enter appliance name ")
cost = float(input("Enter the cost "))
if cost > 1000:
  waranty = cost * 0.01
else: 
  waranty = cost * 0.05
total = cost + waranty 
print("Appliance" + appliance)
print("Cost of appliance $ " + str(cost))
print("Cost of waranty $ " + str(waranty))
print("Total (cost + waranty)" + str(total))
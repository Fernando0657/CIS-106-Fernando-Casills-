name = input("Enter the name of your appliance ")
cost = float(input("Enter the cost of your appliance "))
warranty = 0
total = cost + warranty 
if  cost>1000:
  warranty = cost * .10 
  print("The cost of your warranty is " + str(warranty))
elif cost<1000:
  warranty = cost * .05
  print("The cost of your warranty is " + str(warranty))
else: 
  print("The information you entered is not valid")
  print("The total of appliance & warranty is ")

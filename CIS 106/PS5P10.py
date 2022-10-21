nooforders = 0 
sumofdiscamt = 0
print ("Do you want to calculate total order with discounts (Yes or No) ")
response = input ()
while response == "Yes":
  qty = float(input())
  price = float(input())
  extprice = qty * price
  if extprice > 10000.00:
      discamt = extprice * 0.25
  else:
    discamt = extprice * 0.25
else:
  discamt = extprice * 0.10
  totalorder = extprice - discamt
  sumofdiscamt = sumofdiscamt + discamt
  nooforders = nooforders + 1
  print ("Extended price $ " + str(extprice))
  print ("discount earned $ " + str(discamt))
  print ("Total order amount $ " + str(totalorder))
  print ("Do you want to calculate total order with discounts (Yes or No) ")
  response = input ()
print ("Total discounts given $ " + str(sumofdisct))
print ("Number of orders entered " + str (nooforders))
avgdiscamt = sumofdiscamt / nooforders 
print ("Average discount given $ " + str (avgdiscamt))

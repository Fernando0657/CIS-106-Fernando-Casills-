def train_ticket_price (miles):
  if  miles >= 30: 
     cost = 12.00 
  elif miles >= 20 and miles <= 29:
    cost = 10.00 
  elif miles >= 10 and miles <= 19:
    cost = 8.00 
  else:  
    cost = 5.00 
  train_ticket_price(miles)
  return cost 
response = str(input("Do you want to compute your ticket cost (Y or N )"))
while response == "Y":
  print("Enter your lastname ")
  lastname = input()
  miles = float(input("Enter miles away from downtown chicago "))
  cost = miles
  print("Your ticket cost is $ ", cost)
  print ("Lastname is ", lastname)
  
  reponse = str(input("Do you want to compute your ticket cost (Y or N )"))

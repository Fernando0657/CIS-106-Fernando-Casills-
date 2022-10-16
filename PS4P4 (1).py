numbePerTickets = float(input("Enter the number of tickets "))
if numbePerTickets >= 25:
  costpertik = 50.00
elif numbePerTickets >= 10:
  costpertik = 60.00
elif numbePerTickets >= 5:
  costpertik = 75
else: 
  costpertik = 75 

total = costpertik * numbePerTickets
print("Cost of concert is $ " , total)
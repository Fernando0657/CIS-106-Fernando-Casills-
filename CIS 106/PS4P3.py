principle = float(input("Enter your principle amount"))
years  = int(input("Enter number of years"))
if principle > 100000.00 and years == 5: 
  rate = 0.06 
else:
  if principle >= 50000.00 and principle <= 100000.00 and years == 10:
    rate = 0.05
  else:
    if principle >= 50000.00 and principle <= 100000.00 and years ==5:
      rate = 0.04 
    else: 
      rate = 0.02 

interest = principle * rate 
print("This is your interest $ " + str(interest))
print("This is your principle amount"  + str(principle))
      
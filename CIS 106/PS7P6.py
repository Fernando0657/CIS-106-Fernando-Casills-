def costper (miles):
  cost = miles * 2.5

  return cost 
def gallonsused (miles, gallons):
  mpg = miles / gallons 

  return mpg

# Main 
destination = str(input ("Where was your destination "))
miles = float(input("How many miles did you drive "))
gallons = float(input("How many gallons of gas were used "))
gallonsused (miles, gallons)
costper (miles)
mpg = gallonsused (miles, gallons)
cost = costper(miles) 
print("Your destination was " + destination)
print("Miles per gallon was " + str(mpg))
print("The cost of gas was " + str(cost))


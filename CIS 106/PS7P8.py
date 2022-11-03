def compgross (hours, payrate): 
  if hours > 40: 
    grosspay = (hours - 40) * payrate * 1.5 + 40 * payrate 
  else: 
    gross = hours * payrate 

  return grosspay 

def comppay (jobcode):
  if jobcode =="A": 
    payrate = 30 
  else: 
    if jobcode == "L": 
      payrate = 25 
    else: 
          payrate = 50 
  return payrate 

#Main 
lastname = input("Enter your last name ")
jobcode = input ("Enter your job code (L, A, J ")
hours = float(input("Enter number of hours worked "))
payrate = comppay (jobcode)
grosspay = compgross (hours, payrate)
print("Employee last name " + lastname)
print("Employee gross pay is $ " + str(grosspay))


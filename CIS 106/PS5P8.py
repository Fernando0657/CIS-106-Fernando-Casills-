counter = 0 
print ("Enter do you want to compute your gross income (Yes or No)") 
response = input ()
while response == "Yes": 
  counter = counter + 1 
  print ("Enter employee last name")
  lastname = input ()
  print ("Enter hours worked")
  hoursw = float(input())
  print ("Enter pay rate")
  rate = float(input())
  grosspay = hoursw * rate 
  average = hoursw * rate / counter 
  print ("Employee " + lastname + " gross income is " + str(grosspay))
  print ("This is the gross income average " + str(average))
  print ("Do you want to compute your gross income (Yes or No)") 
  response = input ()
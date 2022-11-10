def next_month_forcast ():
  while True:
    print ("Would you like to calculate next month's forcast           (Yes or No)")
    response = str(input())
    if response != "Yes":
      break 
    else:
      lastname = str(input("Enter last name "))
      month = str(input("Enter 3 charter month (Jan) "))
      sales = float(input("Enter sales ammount "))
    
  
    
  
    if month == "Jan" or month == "Feb" or month == "Mar": 
      per = sales * 1.10
    elif month == "Apr" or month == "May" or month == "Jun":
      per = sales * 1.15
    elif month == "Jul" or month == "Aug" or month == "Sep":
      per = sales * 1.20
    elif month == "Oct" or month == "Nov" or month == "Dec":
      per = sales * 1.25



    print("Student last name is ", lastname)
    print("Next month sales are $ ", str(per))

next_month_forcast()

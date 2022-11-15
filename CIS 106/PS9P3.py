def sales_report (sales): 
  if sales > 100000.00:
    per = 0.10
    commission = sales * 0.10 
  elif sales <= 100000.00:
    per = 0.05
    commission = sales * 0.05
  nextyears = sales * 0.05 
  return commission,nextyears

salesperson = input("Enter sales person name")
lastname = input("Enter lastname ")
sales = float(input("Enter sales ammount "))
commission,nextyears = sales_report(sales)
print("This is your commission", commission)
print("This is your next years report ", nextyears)


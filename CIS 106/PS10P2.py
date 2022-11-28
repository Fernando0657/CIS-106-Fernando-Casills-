def displayarrays(lname, salaries):
    for i in range (0, 10):
      print (lname[i], "Has salary of " ,salaries[i])
 

def rdisplay(lname):
    for i in range (9, -1, -1):
      print (lname[i])

lname = ["Johnson" , "Smith" , "Casillas" , "Miller" , "Davis" , "Brown" , "Jones" , "Garcia" , "Trump" , "Hamani"]
salaries = [50000.00, 25000.00, 55000.00, 35000.00, 65000.00, 75000.00, 20000.00, 100000.00, 90000.00, 150000.00]
displayarrays(lname, salaries)
print ("These are the last names in resevered order")
rdisplay(lname)

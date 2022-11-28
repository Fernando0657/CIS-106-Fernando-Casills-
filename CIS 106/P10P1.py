def displayarrays(lname):
    for i in range (0, 10):
      print (lname[i])
 

def rdisplay(lname):
    for i in range (9, -1, -1):
      print (lname[i])

lname = ["Johnson" , "Smith" , "Casillas" , "Miller" , "Davis" , "Brown" , "Jones" , "Garcia" , "Trump" , "Hamani"]

displayarrays(lname)
print ("These are the last names in resevered order")
rdisplay(lname)

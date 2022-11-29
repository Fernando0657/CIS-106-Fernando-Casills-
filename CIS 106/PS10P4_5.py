def loadarrays(lname3, salary):
  f = open("myfile.txt", "r")
  for i in range (0,10,1):
    ln = f.readline()
    ln = ln.rstrip("\n")
    lname3.append(ln)
    s = f.readline()
    s.rstrip("\n")
    salary.append(s)
  f.close()
def darrays(lname3, salaries):
   for i in range (0, 10, 1):
      print(lname3[i], " has salary of ", salaries[i])
def hilow (lname, salaries):
  hisal = 0.0
  hisub = 0
  losal = 999999.99
  losub = 0
  for i in range (0, 10, 1):
     if salaries[i] > hisal:
        hisal = salaries[i]
        hisub = i 
     elif salaries[i] < losal:
       losal = salaries[i]
       losub = i  

  print (lname[hisub], " has the highest salary of ", salaries[hisub])
  print (lname[losub], " has the lowest salary of ", salaries[losub])
       


def displayarrays (lname, salaries):
    for i in range (0, 10, 1):
      print(lname[i], " has salary of ", salaries[i])

    print ("Another Display using for loops")
    for x in range(2,10,1):
      print (lname[x])
 
    for j in lname:
      print (j)

def rdisplay (lname):
   for i in range (9,-1,-1):
      print (lname[i])

   print (lname)
   lname2 = lname[::-1]
   print (lname2)
   lname.reverse()
   print (lname)


def searchname(lname3, salaries, slname):
  foundsub = -1 
  for i in range (0,10,1):
     if lname3[i] == slname:
          foundsub = i 
  if  foundsub == -1: 
       print (slname, " not in the list ")
  else: 
      print (lname3[foundsub], " has salary of ", salaries[foundsub])



lname = ["Johnson" , "Smith" , "Casillas" , "Miller" , "Davis" , "Brown" , "Jones" , "Garcia" , "Trump" , "Hamani"]
salaries = [50000.00, 25000.00, 55000.00, 35000.00, 65000.00, 75000.00, 20000.00, 100000.00, 90000.00, 150000.00]




lname3 = []
salary = []

loadarrays(lname3, salary)
darrays (lname3, salary)
hilow(lname, salaries)

response = input("Do you want to search for a last name (Y or N ")
while response == "Y":
  slname = input("Enter last name you want to search ")
  searchname(lname3, salaries, slname)
  response = input("Do you want to search for a last name (Y or N ")
  
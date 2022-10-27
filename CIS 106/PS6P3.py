f = open("data3.txt", "r") 
totalbonus = 0 
c = 0 
lastname = f.readline()
while lastname != "": 
  salary = float(f.readline())
  if salary >= 100000.00: 
    bonusrate = 0.20 
  elif salary >= 50000.00:
    bonusrate = 0.15 
  else: 
    bonusrate = 0.10
  bonus = salary * bonusrate
  print("Employe last name", lastname)
  print("Employe bonus: $", format(bonus, '10,.2f'))
  print("Employe salary: $", format(salary, '10,.2f'))
  totalbonus = totalbonus + bonus 
  c = c + 1 
  lastname = f.readline()
f.close()
avgbonus = totalbonus / c 
print(" ")
print("The average bonus is: $ ",            avgbonus)
format(float(avgbonus), '10,.2f')


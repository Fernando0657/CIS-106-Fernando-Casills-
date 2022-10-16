lastName = input("Enter your last name ")
salary = float(input("Enter your yearly salary "))
jobLevel = float(input("Enter your job level "))
if jobLevel >= 10: 
  bonusRate = 0.23
else: 
    if jobLevel >= 5:
      bonusRate = 0.2
    else:
     bonusRate = 0.1
bonus = salary * bonusRate
print("Employee last name " + lastName)
print("Employee bonus $ " + str(bonus))


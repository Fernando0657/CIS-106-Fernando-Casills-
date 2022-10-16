grossIncome = float(input("Enter gross income "))
numberOfDependents = float(input("Enter number of dependents "))
lastname = input("Enter your last name ")
adjustedGrossIncome = grossIncome - numberOfDependents * 12000
if grossIncome > 50000:
  taxRate = 0.2
else: 
  taxRate = 0.1
tax = adjustedGrossIncome * taxRate
if tax < 0:
  tax = 100.0

print("Last Name" + lastname)
print("Gross Income $ " + str(grossIncome))
print("Number of dependents" + str(numberOfDependents))
print("Adjusted Gross Income $ " + str(adjustedGrossIncome))

      
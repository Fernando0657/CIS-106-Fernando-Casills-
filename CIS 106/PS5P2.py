#Calculate discount price 

price = float(input("Please enter item cost"))
percentage = float(input("Enter discount percentage "))

total = price - price * percentage / 100 

print("This is your discounted price$" , total)


def squareft (length, width, height):
  squareft = (2 * length * width + 2 * length * height + 2 * width * height)
  return total 


print ("Would you like to calculate next month's forcast (Yes or No)")
response = str(input())
while response == "Yes": 
  length = float(input("Enter the length of the room "))
  width = float(input("Enter the width of the room "))
  height = float(input("Enter the height of the room "))
  squareft = (2 * length * width + 2 * length * height + 2 * width * height)
  gallons = squareft / 50 
  print("This is the squared feet of your room ", squareft)
  print("You will need this many gallons ", gallons)
  print ("Would you like to calculate square foot of the room (Yes or No)")

counter = 0
print("Do you want to compute your average test score (Yes or No) ")
response = input()
while response == "Yes": 
  counter = counter + 1
  print ("Enter student last name ")
  lastname = input ()
  print ("Enter score 1 ")
  score1 = float(input())
  print ("Enter score 2 ")
  score2 = float(input())
  average = (score1 + score2) / 2
  print("Student " + lastname + " has average of " + str(average))
  print("Do you want to compute your average test score (Yes or No)")
  response = input ()
print ("Total number of students" + str(counter))

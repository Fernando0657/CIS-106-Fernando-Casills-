def b_average (score1,score2,score3):
  sum = score1 + score2 + score3
  average = (sum / 3)
  return average 



lastname = str(input("Enter bowlers last name ")) 
score1 = float(input("Enter your score 1 "))
score2 = float(input("Enter your score 2 "))
score3 = float(input("Enter your score 3 ")) 
average = b_average(score1,score2,score3) 
subtract = 210 - average 
handicap = subtract * 0.90
print("Your last name ", lastname)
print("Your score average is ", average)
print("Your handicap ", handicap)


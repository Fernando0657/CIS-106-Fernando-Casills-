
class Students: 
  def __init__(self, first, last, district, credits):
      self.first = first
      self.last = last 
      self.district = district 
      self.credits = credits 

stu_1 = Students('Fernando', 'Casillas', 'I', '23')
stu_2 = Students('Theadore', 'Smith', 'O', '40')
stu_3 = Students('Gio', 'Soehn', 'I', '30')

print(stu_1)
print(stu_2)
print(stu_3)

stu_1.first = 'Fernando'
stu_1.last = 'Casillas'
stu_1.disctrict = 'I'
stu_1.credits = '23'


stu_2.first = 'Theadore'
stu_2.last = 'Smith'
stu_2.disctrict = 'O'
stu_2.credits = '40'


stu_3.first = 'Gio'
stu_3.last = 'Soehn'
stu_3.disctrict = 'I'
stu_3.credits = '30'

def tuiton (student):
  


  if student.district == "I":
    tuiton = 250.00 * float(student.credits)
  elif student.district == "O":
    tuiton = 500.00 * float(student.credits)
  return tuiton 

#if stu_2.district == "I"
  #tuiton = 250.00 * stu_2.credits
  #elif: stu_2.district == "O"
  #tuiton = 500.00 * stu_2.credits


#if stu_3.district == "I"
 # tuiton = 250.00 * stu_3.credits
  #elif: stu_3.district == "O"
  #tuiton = 500.00 * stu_3.credits

print("Student firstname ", stu_1.first)
print("Student lastname ", stu_1.last)
print("Tuiton cost ", tuiton(stu_1))


print("Student firstname ", stu_2.first)
print("Student lastname ", stu_2.last)
print("Tuiton cost ", tuiton(stu_2))


print("Student firstname ", stu_3.first)
print("Student lastname ", stu_3.last)
print("Tuiton cost ", tuiton(stu_3))

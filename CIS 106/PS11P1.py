def dl1 (myList):
  num = int(input("Number of items for your list "))
  for n in range (0,num,1):
    s = int(input("Enter an integer "))
    mylist.append(s)
  return mylist 
def displaylist(myList):
  for item in mylist:
      print(item)

#main
mylist = [100]
mylist = dl1(mylist)
displaylist(mylist)
print(mylist)

#DL2
mylist.insert(0,99)
print(mylist)
#DL3
mylist[0] = 100
print(mylist) 
#DL4
mylist2 = [500, 600, 700, 800, 900]
mylist2.extend(mylist)
print(mylist2)
#DL5
mylist2.remove(800)
print(mylist2)
#skipped number 6 
#DL6
mylist3 = ["A", "B", "C", "A", "A", "C", "A"]
mylist3.extend(mylist)
print(mylist3)

print ("Count of A grades in list ", mylist3.count ("A"))
location = mylist3.index("B")
print(f"The location of B is at index number {location}.") 

if "F" not in mylist3: 
  print ("F is not in the list ")

mylist2.clear()
print(mylist2)

players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
print(players.sort())
players2 = players.copy()
players2.reverse()
print(players2)

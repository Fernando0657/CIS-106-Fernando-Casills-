f = open("p4d.txt", "r") 

#initialize counters and sums to 0 
c = 0.0
totp_ex = 0.0 

#get first data line 
item = str(f.readline().rstrip('\n'))

while item !="": 
  qty = float(f.readline())
  price = float(f.readline())

  ep = qty*price
  totp_ex = totp_ex + ep 
  c = c+1 

  print("Item is:               ", item) 
  print("Quantity is:           ", qty) 
  print("Price is:              ", price) 
  print("Extended price is:     ", ep)

  item = str(f.readline().rstrip('\n')) 
print("Total Extended Price:   ", totp_ex) 
print("Number of Orders:       ", c)
avg = totp_ex / c 
print("Average Order:          ", avg) 

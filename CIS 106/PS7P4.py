def battingavg(hits, bats): 
    avg = hits / bats 

    return avg 

lastname = str(input("Please enter last name "))
hits = float(input("Enter number of hits "))
bats = float(input("Enter number of bats "))
avg = battingavg(hits, bats)
print ("Student last name " + lastname)
print ("Student batting average was " + str(avg))

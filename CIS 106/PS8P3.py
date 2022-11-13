def out_door_price (make,model,electric,msrp):
    if  make == "Honda" or make =="Accord":
      p_off_msrp = 0.10
    elif make == "Toyota" or make == "Rav4":
      p_off_msrp = 0.15
    elif make == "Electric":
      p_off_msrp = 0.30
    else:
      p_off_msrp = 0.05 
    amt = p_off_msrp * msrp 
    tax = 0.07 * msrp
    total = msrp - amt  + tax 
    return total
totalmsrp = 0 
totasp = 0
response = input("Do you want to compute msrp of car (Y or N)")
while response == "Y":
    print("Enter make of car")
    make = input()
    print("Enter model")
    model = input()
    print("Is it an electric car (Y or N")
    electric = input()
    print("Enter MSRP")
    msrp = float(input())
    total = out_door_price(make,model,electric,msrp) 
    print("Total owed is $ ", total)
    totalmsrp = totalmsrp + msrp 
    totasp = totasp + total
    response = input("Do you want to compute msrp of car (Y or N)")
    
print("Your msrp is $ ", totalmsrp)
print("Your total asking price $ ", totasp)

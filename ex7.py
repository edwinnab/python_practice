price = eval(input("Whats the meal price:"))
tip = eval(input("how much tip would you leave:"))
btip = tip/100
bill = price+btip
print("Your tipAmount=", btip, "totalbill=", bill)

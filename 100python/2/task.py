print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? €"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? %"))
people = float(input("How many people to split the bill ? "))
print("Each person should pay: €"+  str((bill + (bill*tip/100))/people))



print(f"Each person should pay: €{round(((bill) + (bill*tip/100))/people, 2)}")
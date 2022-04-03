print("Welcome to the tip calculator.")
bill= float(input("What was the total bill? £"))
percent= int(input("What percentage tip would you like to give? 10, 12, or 15? "))
numbpeople=int(input("How many people to split the bill? "))
ratio=1+(percent/100)
totalbill=bill*ratio
eaperson=round(totalbill/numbpeople,2)
print(f"Each person should pay: £{eaperson}")
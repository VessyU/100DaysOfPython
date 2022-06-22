from replit import clear
from art import logo
#import copy #copy to stop dictionary changing size during iteration
print(logo)
bids={}
final_winner=False #in case there is a draw


while final_winner==True:
  name = input("What is your name?: ")
  price = input("What's your bid?: £")
  bids[name]=price
  restart = input("Are there any other bidders? Type 'yes' or 'no': ")
  if restart == "yes":
    clear()
  if restart == "no":
    more_bidders=True
  winners_bid=0 #temp
  winners_name="temp"

  for x in bids:
    if int(bids[x]) > winners_bid:
      winners_bid=int(bids[x])
      winners_name=x
    temp_bid=int(bids[x])
    temp_bidder=x
    if temp_bid==winners_bid and temp_bidder!=winners_name:
      final_winner=True
      clear()
      print("This round of bidding ends in a draw, lets go againnnnn.\n")
    
  
print(f"The winner is {winners_name} with a bid of £{winners_bid}")
  






    
from art import logo
import random
import string
from replit import clear

player_score=0
dealer_score=0

deck={"A":11,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10} #starts with ace cause it is first!

def blackjack():
  playgame=True
  players_cards=[]
  dealers_cards=[]
  random_choice=random.choice(list(deck))
  dealers_cards+=random.choice(list(deck))
  clear()
  for x in range(2):
    players_cards.append(random_choice)
  print(logo)
  print(f"Your cards: {players_cards}")
  print(f"Dealer's first card: {dealers_cards}")
  player_score = deck.get(players_cards[0]) + deck.get(players_cards[1])
  dealer_score = deck.get(dealers_cards[0])
  if player_score == 21:
    return print("Congrats, you win many moneyz! ")
  while playgame==True:
    p_hit=input("Type 'y' to get another card, type 'n' to pass: ")
    if p_hit =="n":
      break
    if p_hit == "y":
      players_cards.append(random.choice(list(deck)))
      print(f"Your cards: {players_cards}")
      player_score = 0
      ace = 0
      pclen=len(players_cards)
      for x in range(pclen):
        p_score = deck.get(players_cards[x])
        player_score += p_score
      for x in players_cards: # need to account for ace possibly being 1 instead of 11, + blackjack is typically played with multiple decks so no need to worry if over 4 aces etc..
        if x == "A":
          ace += 1
        if ace > 0 and player_score > 21:
          ace -= 1
          player_score -=10
      if player_score > 21:
        return print("Bust!")
      elif player_score==21:
        return print("Congrats, you win many moneyz! ")
  while dealer_score < player_score:
    dealer_score=0
    ace=0
    dealers_cards+=random_choice
    dclen=len(dealers_cards)
    print(f"Dealer hits: {dealers_cards}")
    for x in range(dclen):
      d_score = deck.get(dealers_cards[x])
      dealer_score += d_score
    for x in dealers_cards: 
      if x == "A":
        ace += 1
      if ace > 0 and dealer_score > 21:
        ace -= 1
        dealer_score -=10
    if dealer_score == 21:
      return print("Dealer wins. Better luck next time! ")
    elif (dealer_score >= 16) & (dealer_score==player_score):
      return print("Draw! lets go again.")
    elif dealer_score>21:
      return print("Dealer busts! You win. ")
    elif dealer_score>player_score:
      return print("Dealer wins. Better luck next time! ")

print(logo)
playagain=True
play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while playagain==True:
  blackjack()
  play_again=input("Do you want to play again? Type 'y' or 'n': ")
  if play_again == "n":
    break
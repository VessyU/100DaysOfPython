import random

def number_guessing_game():
  print("Welcome to the Number Guessing Game! ")
  print("I'm thinking of a number between 1 and 100. ")
  hard_or_easy = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  computer_choice = random.randint(1,100)
  if hard_or_easy == "easy":
    lives = 10
  if hard_or_easy == "hard":
    lives = 5
  for x in range(lives):
    guess = int(input(f"You have {lives} attempts remaining to guess the number. "))
    if guess > computer_choice:
      lives -= 1
      if lives == 0:
        return print("\nYou've run out of tries, you will die in 5, 4, 3...")
      print("Too high.\nGuess again. ")
    if guess < computer_choice:
      lives -= 1
      if lives == 0:
        return print("\nYou've run out of tries, you will die in 5, 4, 3...")         
      print("Too low.\nGuess again. ")
    if guess == computer_choice:
      return print(f" \nYou got it! The answer was {computer_choice}. ")

number_guessing_game()
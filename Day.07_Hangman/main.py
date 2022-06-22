import random
from hangman_art import stages, logo
from hangman_words import list_of_words
from replit import clear

print(logo)
game_is_finished = False
lives = len(stages) - 1


random_word=random.choice(list_of_words)
length_of_word=len(random_word)

list_of_word=list(random_word)
list_of_attempt = []

for blank in range(length_of_word):
  list_of_attempt += "_"
print(' '.join(list_of_attempt))

while game_is_finished is not True:

  guess = input("What letter would you like to try? ").lower()
  clear()
  if guess in list_of_attempt:
    print("You've already guessed this letter!")

  for position in range(length_of_word):
    if guess == list_of_word[position]:
      list_of_attempt[position] = guess
      #words = [list_of_random_word.replace('', '[guess]') for w in words]
  print(' '.join(list_of_attempt))

  if guess not in list_of_word:
    print(f"{guess} is not in the word, better luck next time!")
    lives -= 1
    if lives == 0:
      game_is_finished = True
      clear()
      print(f"You lose! \n \nThe word was {random_word}.")
  if "_" not in list_of_attempt:
    game_is_finished = True
    clear()
    print("Congrats you win!!!")
    
  print(stages[lives])

print(f"The word was {random_word}.")
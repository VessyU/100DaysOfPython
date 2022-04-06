import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice=int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

computer_choice= random.randint(0,2)
if computer_choice==0:
  print(f"""
 Computer chose:
 {rock}""")

if computer_choice==1:
  print(f"""
 Computer chose:
 {paper}""")

if computer_choice==2:
  print(f"""
 Computer chose:
 {scissors}""")
win=[-2,1]
lose=[-1,2]
if choice-computer_choice==0:
  print("You draw :/")

elif choice-computer_choice==win[0] or choice-computer_choice==win[1]:
  print("You win!")

elif choice-computer_choice==lose[0] or choice-computer_choice==lose[1]:
  print("You lose :(")

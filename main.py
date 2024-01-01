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

import random
game=[rock,paper,scissors]
user=int(input("0 for Rock, 1 for Paper, 2 for Scissors \n"))
chosen_name=game[user]
print(chosen_name)
print("Computer Chose")
choice=random.randint(0,2)
computer = game[choice]
print(computer)
if user >= 3 or user < 0:
  print("Try again")
elif user == 0 and choice == 2:
  print("You Win")
elif user == 2 and choice == 0:
  print("You Lose")
elif choice > user:
  print("You Lose")
elif user > choice:
  print("you Win")
elif user == choice:
  print("you draw")

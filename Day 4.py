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

user_choice=int(input("Enter your choice: Type 0 for Rock,1 for Paper and 2 for Scissors\n"))

computer_choice=random.randint(0,2)
games_choice=[rock,paper,scissors]
print("User Chose:\n")
print(games_choice[user_choice])
print("Computer Chose:\n")
print(games_choice[computer_choice])

if (user_choice==0 and computer_choice==2) or (user_choice==2 and computer_choice==1) or (user_choice==1 and computer_choice==0):
  print("User Wins")
elif user_choice==computer_choice:
  print("Draw")
else:
  print("Computer Wins")

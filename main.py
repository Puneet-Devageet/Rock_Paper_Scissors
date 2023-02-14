
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

#Write your code below this line 👇
print("Welcome to Rock Paper Scissor Game!")
store = int(input("What do you want to choose? Press '0 for rock', '1 for paper' and '2 for scissors': "))

game = [rock, paper, scissors]
if store == 0:
    print(f"You choose:\n{game[0]}")
elif store == 1:
    print(f"You choose:\n{game[1]}")
elif store == 2:
    print(f"You choose:\n{game[2]}")
else:
    print("Invalid Input")

game1 = random.choice(game)
print(f"Computer Choose:\n{game1}")

if store == 0 and game1 == game[2]:
    print("You Won!\nOnce More")
elif store == 0 and game1 == game[1]:
    print("You Loss.\nBetter Luck Next Time")
elif store == 1 and game1 == game[2]:
    print("Sorry You lost.")
elif store == 1 and game1 == game[0]:
    print("You Won")
elif store == 2 and game1 == game[1]:
    print("You Won.\nTry Again")
elif store == 2 and game1 == game[0]:
    print("You Loss.\nBetter Luck Next Time")
else:
    print("It's a draw.\nTry Again!")

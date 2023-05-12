# Rock, Paper, Scissors Game:
# Create a game where the user plays against the computer by choosing rock, paper, or scissors.

import random

def play_game():
  choices = ["rock", "paper", "scissors"]

  user_choice = input("Choose rock, paper, or scissors: ").lower()
  computer_choice = random.choice(choices)

  print("You chose " + user_choice + ".")
  print("The computer chose " + computer_choice + ".")

  if user_choice == computer_choice:
    print("It's a tie!")
  elif user_choice == "rock":
    if computer_choice == "scissors":
      print("You win!")
    else:
      print("You lose!")
  elif user_choice == "paper":
    if computer_choice == "rock":
      print("You win!")
    else:
      print("You lose!")
  elif user_choice == "scissors":
    if computer_choice == "paper":
      print("You win!")
    else:
      print("You lose!")
  else:
    print("Invalid choice. Try again.")

play_game()

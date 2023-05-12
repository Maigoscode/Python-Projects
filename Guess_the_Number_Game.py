# Guess the Number Game:
# Create a game where the computer generates a random number
# and the user has to guess it.

import random

num = random.randint(1, 50)
guess = None
# implement loop
while guess != num:
  guess = int(input("Guess a number between 1 and 50: "))
  if guess < num:
    print("Too low, try again.")
  elif guess > num:
    print("Too high, try again.")
  else:
    print("You guessed it!")
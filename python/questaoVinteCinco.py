# this is a guess the number game.

import random
print("Hello. What is you name?")
name = input()
secretNumber = random.randint(1,20)
print("Well, " + name + ", I am thinking of a number between 1 and 20. Take a guess.")

# aks the player to guess 6 times.

for guessesTaken in range(1,7):
      print("Take a guess.")
      guess = int(input())
      if guess < secretNumber:
          print("You guess is too low.")
      elif guess > secretNumber:
          print("You guess is too high.")
      else:
          break # this condition is the correct guess!

if guess == secretNumber:
    print("Good job, " + name + "! You guessed my number.")
else:
    print("Nope.The number I was thinking of was" + str(secretNumber))

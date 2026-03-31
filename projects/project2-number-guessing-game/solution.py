# Project 2 — Number Guessing Game
# Author: your name here

import random

# TODO: generate a random secret number between 1 and 10
secret_number = random.randint(1, 10)
# TODO: set up a guesses counter
guesses_count = 0
# TODO: get the user's first guess
guess = int(input("Guess the number (between 1 and 10): "))
guesses_count += 1
# TODO: while loop — keep asking until the guess is correct
while guess != secret_number:
    # – print "Too low!" or "Too high!" on each wrong guess
    if guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
#   - count each guess
guess = int(input("Try again: "))
    guesses_count += 1
# TODO: print the congratulations message with the number of guesses
print(f"Congratulations! You guessed the number {secret_number} in {guesses_count} tries.")
import random

number = random.randint(1, 100)
guess = input("Guess the number (between 1 and 100): ")

while not guess.isdigit() or int(guess) < 1 or int(guess) > 100:
    print("Invalid guess. Please enter a number between 1 and 100.")
    guess = input("Guess the number (between 1 and 100): ")

guess = int(guess)

if guess == number:
    print("Correct! You guessed the number.")
else:
    print("Incorrect. The correct number was:", number)

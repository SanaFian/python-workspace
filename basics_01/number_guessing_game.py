# ============================================
# Project 01: Number Guessing Game
# ============================================

import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("=== Welcome to the Number Guessing Game! ===")
    print("I have chosen a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.\n")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter an integer.\n")
            continue

        attempts += 1

        if guess == secret_number:
            print(f"🎉 Congratulations! You guessed the number in {attempts} attempts!")
            return
        elif guess < secret_number:
            print("Too low! Try a higher number.\n")
        else:
            print("Too high! Try a lower number.\n")

    print(f"Game Over! The secret number was: {secret_number}")

if __name__ == "__main__":
    play_game()

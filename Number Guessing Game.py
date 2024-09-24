import random

def number_guessing_game():
    number_to_guess = random.randint(1, 50)
    attempts = 0
    guessed = False

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while not guessed:
        user_guess = input("Make a guess: ")

        # Validate input
        if not user_guess.isdigit():
            print("Please enter a valid number.")
            continue

        user_guess = int(user_guess)
        attempts += 1

        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed = True
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")

if __name__ == "__main__":
    number_guessing_game()

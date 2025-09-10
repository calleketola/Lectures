import random

run = True

while run:
    randomized_number = random.randint(3,3)
    guess = input("Guess the number (1-100): ")
    guess = int(guess)
    print(f"You guessed {guess}.")
    if guess == randomized_number:
        print("Your guess was correct!")
    else:
        print("You guessed wrong.")

    if input("Guess again? ").lower() == "yes":
        print("Great")
    else:
        print("Wrong!")

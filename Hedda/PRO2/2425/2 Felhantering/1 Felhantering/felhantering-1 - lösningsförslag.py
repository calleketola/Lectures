import random

run = True

while run:
    randomized_number = random.randint(3,3)
    try:
        guess = input("Guess the number (1-100): ")
        guess = int(guess)
    except ValueError:
        print("You must answer with a whole number")
        continue
    except KeyboardInterrupt:
        print("Nope, you don't get away that easily")
        continue
    except EOFError:
        print("The file mysteriously ended. Not the program though!")
        continue
    print(f"You guessed {guess}.")
    if guess == randomized_number:
        print("Your guess was correct!")
    else:
        print("You guessed wrong.")

    if input("Guess again? ").lower() == "nej":
        print("Sneaky att man måste svara på svenska va?")
        run = False
    else:
        print("Then we go again!")

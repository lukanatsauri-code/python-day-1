import random

print("Day 3 - Guess the number")
print("I'm thinking of a number from 1 to 100.")
print("Type q to quit.")
print("You have 10 tries. \n")

secret = random.randint(1, 100)
max_attempts = 10
attempts = 0
won = False
quit_game = False

while attempts < max_attempts:
    guess_text = input("Enter your guess (1-100): ")

    if guess_text.lower() == "q":
        quit_game = True
        break 

    try:
        guess = int(guess_text)
    except ValueError:
        print("Please type a whole number (or q to quit). \n")
        continue 

    if guess < 1 or guess > 100:
        print("Out of range. Enter a number from 1 to 100. \n")
        continue 

    attempts = attempts + 1

    if guess < secret:
        print("Too low.")
    elif guess > secret:
        print("Too high.")
    else:
        won = True
        break 

    print("Tries used: ", attempts, "of", max_attempts, "\n")


if quit_game:
    print("\nYou quit. The number was", secret)
elif won:
    print("\nCorrect! you guessed it in", attempts, "tries.")
else:
    print("\nOut of tries. The number was", secret)

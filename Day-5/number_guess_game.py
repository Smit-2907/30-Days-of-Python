# This program is a simple number guessing game where the user has to guess a predefined number until they get it right.
num = 43
while True:
    guess = int(input("Enter the number:"))
    if guess == num:
        print("Congratulations! You guessed the number.")
        break
    elif guess < num:
        print("Too low! Try Agian!")
    else:
        print("Too High! Try Again!")
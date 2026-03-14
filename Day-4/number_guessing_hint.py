secrat_number = 69
guess = int(input("Guess the secret number: "))
if guess < secrat_number:
    print("Too low! Try again.")
elif(guess > secrat_number):
    print("Too high! Try again.")
else:
    print("Congratulations! You've guessed the secret number!")
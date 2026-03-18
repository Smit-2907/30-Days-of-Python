print("\nExercise 5 — Even or Odd Number ")
def odd_even(num):
    if num % 2 == 0:
        print("The number is Even")
    else:
        print("The number is Odd!!")

number = int(input("Enter an integer to check: "))
odd_even(number)
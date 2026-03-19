### Exercise 3 — Filter Even Numbers
# Use lambda to filter even numbers from a list.
number = int(input("Enter number: "))
odd_even = lambda a : "Even Number" if a % 2 == 0 else "Odd Number"

print(odd_even(number))
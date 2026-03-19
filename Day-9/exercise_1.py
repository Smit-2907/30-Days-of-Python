# This is a function that takes any number of inputs and returns the sum.
def sum(*number):
    total = 0
    for i in numbers:
        i = int(i)
        total = total + i
    print("Sum is:", total)

numbers = input("Enter the numbers with space: ").split()
sum(numbers)
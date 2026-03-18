# This is the program to find factorial numbers with recursion.
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
n = int(input("Enter the number: "))
print("The factorial is:", factorial(n))
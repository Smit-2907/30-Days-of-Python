# This is a simple comprison program that takes two numbers as input and compares them using "if-elif-else" statement.
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

if num_1 > num_2:
    print("Biggest number from these two is: ", num_1)
    print("Smallest number from these two is: ", num_2)
elif num_2 > num_1:
    print("Biggest number from these two is:", num_2)
    print("Smallest number from these two is: ", num_1)
else:
    print("Both numbers are equal.")
# Exercise 1 — Prime Number Checker
print("Exercise 1 - Prime Number Checker")
num = int(input("Enter a number to check it is prime or not: "))
for i in range(2, num):
    if num % i == 0:
        print("This is not a prime number", num)
        break
    else:
        print("This number is a prime number", num)
        break

# Exersice 2: Login System
count = 0
correct_password = "admin_123"
print("Exercise 2: Login System")
while True:
    if count < 3:
        guess = input("Enter password: ")
        if guess == correct_password:
            print("Access Granted.")
            break
        else:
            print("Access Denied.")
            count += 1
    else:
        print("Your account is blocked")
        break

# Exercise 3: Sum unti zero 
total_sum = 0
while True:
    num = int(input("Enter Number: "))
    if num != 0:
        total_sum = total_sum + num
    else:
        print("The sum is: ", total_sum)
        break

# Exercise 4: print the pattern
# *
# **
# ***
# ****
# *****
for i in range(1, 6):
    for j in range(0, i):
        print("*", end="")
    print("\n")

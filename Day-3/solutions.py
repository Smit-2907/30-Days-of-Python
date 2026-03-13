# Exercise 1: Divisible Checker
print("Exercise 1: Divisible Checker")
number= int(input("Enter a absolute number to check if it is divisable by 7 or not: "))
if number % 7 == 0:
    print("Divisible by 7.")
else:
    print("Not divisible by 7.")

# Exercise 2: Password Checker
print("\nExercise 2: Password Checker")
password = input("Enter password: ")
if password == "admin":
    print("Access Granted.")
else:
    print("Access Denied.")

# Exercise 3: Age Category Program
print("\nExercise 3: Age Category Program")
age = int(input("Enter your age: "))
if age <= 0:
    print("Invalid age.")
elif age < 13:
    print("Child.")
elif age >= 13 and age <=19:
    print("Teenager.")
elif(age >=20 and age <= 59):
    print("Adult.")
else:
    print("Senior.")
# 🐍 Day 3 — Conditional Statements (Decision Making)

## 🎯 Goal
Learn how Python programs make decisions using:
- `if` statements
- `else`
- `elif`
- comparison operators
---
# 🗺️ Day 3 Flow (Follow in Order)

### 1️⃣ Understanding `if` Statement
Create a file: if_demo.py

Write:
```python
age = 18
if age >= 18:
    print("You are eligible to vote")
Run the program and observe the output.

2️⃣ Using else
Create: if_else_demo.py
Write a program that checks if a number is positive or negative.

Example idea:
number = int(input("Enter a number: "))
if number >= 0:
    print("The number is positive")
else:
    print("The number is negative")

3️⃣ Using elif
Create: grade_checker.py
Write a program that checks marks and prints the grade.

Example idea:
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D")

4️⃣ Comparison Operators
Learn how these operators work:
>   greater than
<   less than
>=  greater than or equal
<=  less than or equal
==  equal to
!=  not equal to

Create: comparison_demo.py
Write small examples to test each operator.

5️⃣ Using if with User Input
Create: voting_checker.py
Ask the user for their age and check if they can vote.

Example idea:
Enter your age: 17
You are not eligible to vote

6️⃣ Multiple Conditions
Create: even_odd_checker.py
Write a program that checks if a number is even or odd.
Hint: number % 2

Example idea:
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

7️⃣ Solve the Exercises
Practice by writing small programs:
Exercise 1 — Divisible Checker
Exercise 2 — Password Checker
Exercise 2 — Password Checker 

8️⃣ Mini Challenge
Create: login_system.py
Write a simple program that checks a username.

Example idea:
Enter username: admin
Access Granted

If the username is not correct:
Access Denied
⭐ Optional Bonus

Create: largest_number.py
Ask the user for two numbers and print which one is larger.

Example idea:
Enter first number: 10
Enter second number: 15
15 is the larger number

# ✅ Day 3 Completion Checklist

- [*]Learned if statements
- [*]Used if-else
- [*]Used elif
- [*]Practiced comparison operators
- [*]Built programs with conditions
- [*]Solved exercises
- [*]Completed mini challenge
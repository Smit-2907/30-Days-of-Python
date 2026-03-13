# 🐍 Day 2 — User Input & Type Conversion

## 🎯 Goal
Learn how Python programs interact with users and understand:
- `input()` function
- user interaction
- type conversion (`int`, `float`)
- simple calculations

# 🗺️ Day 2 Flow (Follow in Order)

### 1️⃣ Taking User Input
Create a file: user_input.py
Write:
```python
name = input("Enter your name: ")
print("Hello", name)
Run the file and enter your name when prompted.
```
2️⃣ Taking Multiple Inputs
Create: user_info.py
Write a program that asks the user for:
name
city

Example idea:
Enter your name: John
Enter your city: New York

Output:
Hello John
You live in New York

3️⃣ Understanding the input() Data Type
Create: input_type.py
Write:
```
age = input("Enter your age: ")
print(age)
print(type(age))
```
Observe that input() always returns a string.

4️⃣ Convert Input to Integer
Create: age_program.py
Use int() to convert the input.

Example idea:
age = int(input("Enter your age: "))
print("Next year you will be", age + 1)

5️⃣ Simple Number Calculation
Create: addition.py
Write a program that:
asks the user for two numbers
converts them to integers
prints their sum

Example idea:
Enter first number: 5
Enter second number: 10
Sum is: 15

6️⃣ Working With Float Numbers

Create: float_input.py
Ask the user for their height and convert it to a float.

Example idea:
height = float(input("Enter your height in meters: "))
print("Your height is", height, "meters")

7️⃣ Solve the Exercises
Practice by writing small programs:
Program that asks user name and favorite programming language
Program that asks age and prints age after 5 years
Program that takes two numbers and prints their product

8️⃣ Mini Challenge
Create: simple_calculator.py
Ask the user for two numbers and print:
Addition
Subtraction
Multiplication
Example output idea:

Addition: 15
Subtraction: -5
Multiplication: 50

⭐ Optional Bonus
Create: temperature_converter.py
Ask the user for temperature in Celsius and convert it to Fahrenheit.
Hint:
F = (C × 9/5) + 32

# ✅ Day 2 Completion Checklist

- [*]Took input from user
- [*]Used the input() function
- [*]Converted string to integer
- [*]Converted string to float
- [*]Performed simple calculations
- [*]Solved exercises
- [*] mini challenge
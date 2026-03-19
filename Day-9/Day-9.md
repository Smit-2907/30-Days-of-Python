# 🐍 Day 9 — Function Arguments & Lambda Functions

## 🎯 Goal
Learn how to make functions more flexible using different types of arguments and create short functions using lambda.

Today you will learn:
- Types of function arguments
- Keyword arguments
- Default arguments
- Arbitrary arguments
- Lambda functions

These concepts help write **more flexible and powerful functions**.


# 🗺️ Day 9 Flow (Follow in Order)

### 1️⃣ Positional Arguments
Values are passed in order.
Create a file: `positional_args.py`

Example:
def greet(name, age):
    print(name, "is", age, "years old")

greet("John Doe", 20)

Output:
John Doe is 20 years old

### 2️⃣ Keyword Arguments
Pass values using parameter names.
Create: `keyword_args.py`

Example:
def greet(name, age):
    print(name, "is", age, "years old")

greet(age=20, name="John Snow")

Output:
John DOe is 20 years old

### 3️⃣ Default Arguments
Set default values for parameters.
Create: `default_args.py`

Example:
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("John Doe")

Output:
Hello Guest
Hello John Doe

### 4️⃣ Arbitrary Arguments (*args)
Allows multiple values.
Create: `args_demo.py`

Example:
def add_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    print(total)

add_numbers(1, 2, 3, 4)

Output:
10

### 5️⃣ Lambda Functions
Small one-line anonymous functions.
Create: `lambda_demo.py`

Example:
add = lambda a, b: a + b
print(add(3, 5))

Output:
8

### 6️⃣ Lambda with List
Create: `lambda_list.py`

Example:
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x * x, numbers))
print(squared)

Output:
[1, 4, 9, 16]

# 🧠 Function + Logic Exercises

### Exercise 1 — Sum using *args
Write a function that takes any number of inputs and returns the sum.

Example:
Input:
1, 2, 3, 4

Output:
10

### Exercise 2 — Find Maximum using Function
Find the maximum number from given inputs.

### Exercise 3 — Filter Even Numbers
Create: `filter_even.py`
Use lambda to filter even numbers from a list.

Example:
Input:
[1, 2, 3, 4, 5, 6]

Output:
[2, 4, 6]

### Exercise 4 — Multiply List using Lambda
Multiply each element of list by 2.

### Exercise 5 — Sort List of Tuples
Create: `sort_tuples.py`

Example:
Input:
[(1, 3), (2, 1), (4, 2)]

Output:
[(2, 1), (4, 2), (1, 3)]

Hint:
Sort based on second value.

# 7️⃣ Mini Challenge
Build a program to manage student marks using functions.

Features:
- Add student marks
- Calculate average
- Find highest marks

Example:

Enter marks: 80 90 70 85
Average: 81.25
Highest: 90

Hint:
Use:
- functions
- *args or list
- lambda for calculations

# ✅ Day 9 Completion Checklist

- [ ] Learned types of function arguments
- [ ] Practiced *args and default arguments
- [ ] Learned lambda functions
- [ ] Solved function-based problems
- [ ] Completed mini challenge
- [ ] Pushed code to GitHub
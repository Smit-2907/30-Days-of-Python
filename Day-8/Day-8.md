# 🐍 Day 8 — Functions

## 🎯 Goal
Learn how to write reusable and structured code using functions.

Today you will learn:
- What functions are
- How to create functions
- Parameters and arguments
- Return values

Functions help in writing **clean, reusable, and modular code**.

---

# 🗺️ Day 8 Flow (Follow in Order)

### 1️⃣ What is a Function?
A function is a block of code that runs when called.
Create a file: `function_basics.py`

Example:
def greet():
    print("Hello, welcome!")
greet()

Output:
Hello, welcome!

Explanation:  
`greet()` is a function that runs when called.

### 2️⃣ Function with Parameters
Functions can take input values.
Create: `function_parameters.py`

Example:
def greet(name):
    print("Hello", name)
greet("Smit")

Output:
Hello Smit

Explanation:  
`name` is a parameter.

### 3️⃣ Function with Return Value
Functions can return values.
Create: `function_return.py`

Example:
def add(a, b):
    return a + b

result = add(3, 4)
print(result)

Output:
7

Explanation:  
`return` sends the result back.

### 4️⃣ Default Parameters
Create: `default_parameters.py`

Example:
def greet(name="Guest"):
    print("Hello", name)
greet()
greet("Smit")

Output:
Hello Guest
Hello Smit

### 5️⃣ Multiple Return Values
Create: `multiple_return.py`

Example:
def operations(a, b):
    return a + b, a - b

sum_val, diff_val = operations(5, 3)

print(sum_val)
print(diff_val)

Output:
8
2

# 🧠 Function-Based Exercises

### Exercise 1 — Even or Odd Function
Write a function that checks if a number is even or odd.

### Exercise 2 — Factorial Function

### Exercise 3 — Sum of List

### Exercise 4 — Maximum Number in List

### Exercise 5 — Check Prime Number

# 7️⃣ Mini Challenge
Create: `calculator_function.py`
Build a simple calculator using functions.

Features:
- Add
- Subtract
- Multiply
- Divide

Example:
Enter first number: 5
Enter second number: 2

1. Add
2. Subtract
3. Multiply
4. Divide

Output:
Result: 10

Hint:
Create separate functions like:
- add()
- subtract()
- multiply()
- divide()

# ✅ Day 8 Completion Checklist
- [ ] Learned function basics
- [ ] Practiced parameters and return values
- [ ] Used default parameters
- [ ] Solved function-based problems
- [ ] Completed mini project
- [ ] Pushed code to GitHub
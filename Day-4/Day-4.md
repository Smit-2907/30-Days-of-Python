# 🐍 Day 4 — Loops (for, while)

## 🎯 Goal
Learn how to repeat tasks using loops.  
Loops allow programs to execute a block of code multiple times.

Today you will learn:

- `for` loops
- `while` loops
- `range()` function
- simple loop based programs

---

# 🗺️ Day 4 Flow (Follow in Order)

### 1️⃣ Understanding `for` Loop
Create a file: `for_loop_demo.py`

Example:
```python
for i in range(5):
    print(i)

Output:
0
1
2
3
4

Explanation:
range(5) generates numbers from 0 to 4
the loop runs 5 times

2️⃣ Printing Numbers
Create: print_numbers.py
Write a program that prints numbers from 1 to 10.

Example output:
1
2
3
4
5
6
7
8
9
10

3️⃣ Multiplication Table
Create: multiplication_table.py
Write a program that asks the user for a number and prints its multiplication table.

Example:
Enter number: 5

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50

Hint:

for i in range(1, 11):

4️⃣ Understanding while Loop
Create: while_demo.py

Example:
count = 1
while count <= 5:
    print(count)
    count += 1

Output:
1
2
3
4
5

Explanation:
the loop runs while the condition is true

5️⃣ Countdown Program
Create: countdown.py
Write a program that prints a countdown.

Example:
5
4
3
2
1
Go!

Hint:
number -= 1

6️⃣ Solve the Exercises

Write small programs for practice:
print numbers 1 to 20
print even numbers from 1 to 20
calculate sum of numbers from 1 to 100

7️⃣ Mini Challenge
Create: number_guessing_hint.py

Write a simple program that:
stores a secret number
asks the user to guess
tells them if the guess is too high or too low

Example:
Guess the number: 7
Too low
# 🐍 Day 5 — Loop Control Statements

## 🎯 Goal
Learn how to control loop execution using special statements.

Today you will learn:
- `break`
- `continue`
- `pass`

These statements help control how loops behave while running.
---

# 🗺️ Day 5 Flow (Follow in Order)

### 1️⃣ Understanding `break`

`break` immediately stops a loop.
Create a file: `break_demo.py`

Example:
```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)

Output:
1
2
3
4

Explanation:
The loop stops once i becomes 5.

2️⃣ Understanding continue
continue skips the current loop iteration.
Create: continue_demo.py

Example:
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

Output:
1
2
4
5

Explanation:
When i becomes 3, Python skips that iteration.

3️⃣ Understanding pass
pass does nothing.
It is used as a placeholder.
Create: pass_demo.py

Example:
for i in range(5):
    if i == 2:
        pass
    print(i)

Output:
0
1
2
3
4

4️⃣ Loop with User Input
Create: password_checker.py
Write a program that keeps asking for a password until the correct one is entered.

Example idea:
Enter password: test
Wrong password

Enter password: python123
Access granted

Hint: use a while loop + break

5️⃣ Stop a Loop with break
Create: stop_loop.py
Write a program that prints numbers from 1 to 100 but stops when the number reaches 50.

Example output:
1
2
3
...
49

6️⃣ Skip Even Numbers

Create: skip_even_numbers.py
Write a program that prints numbers from 1 to 20 but skips even numbers.

Example output:
1
3
5
7
9
...
19

Hint:
if number % 2 == 0:

Exercise 1 — Prime Number Checker
Exercise 2 — Login System (3 Attempts)
Exercise 3 — Number Guessing Game

7️⃣ Mini Challenge
Create: number_guess_game.py
Build a simple guessing program:
store a secret number
ask the user to guess
repeat until correct

Example:
Guess the number: 5
Wrong guess
Guess the number: 8
Correct!

Hint:
use while
use break when correct

✅ Day 5 Completion Checklist

- [*] Learned break
- [*] Learned continue
- [*] Learned pass
- [*] Built loop control programs
- [*] Solved exercises
- [*] Completed mini challenge
# 🐍 Day 7 — Lists

## 🎯 Goal
Learn how to work with lists and perform operations on collections of data.

Today you will learn:
- List basics
- Indexing and slicing
- List methods
- Looping through lists

You will also solve **array-based problems (DSA)** to build logic.

---

# 🗺️ Day 7 Flow (Follow in Order)

### 1️⃣ Creating Lists
A list is a collection of items.
Create a file: `list_basics.py`

Example:
numbers = [1, 2, 3, 4, 5]
names = ["John", "David", "Ramesh"]
print(numbers)
print(names)

Output:
[1, 2, 3, 4, 5]
['Smit', 'Rahul', 'Amit']

### 2️⃣ List Indexing
Access elements using index.
Create: `list_indexing.py`

Example:
numbers = [10, 20, 30, 40]

print(numbers[0])
print(numbers[2])

Output:
10
30

---

### 3️⃣ List Slicing
Extract parts of a list.
Create: `list_slicing.py`

Example:
numbers = [1, 2, 3, 4, 5]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])

Output:

[2, 3, 4]
[1, 2, 3]
[3, 4, 5]

---

### 4️⃣ Important List Methods
Create: `list_methods.py`

Example:
numbers = [1, 2, 3]

numbers.append(4)
numbers.insert(1, 10)
numbers.remove(2)

print(numbers)

Output:
[1, 10, 3, 4]

Explanation:
- `append()` → adds element at end  
- `insert()` → adds element at specific position  
- `remove()` → removes element  

---

### 5️⃣ Looping Through Lists
Create: `loop_list.py`

Example:
numbers = [1, 2, 3, 4]

for num in numbers:
    print(num)

Output:
1
2
3
4

---

# 🧠 Array Algorithm Exercises (DSA)

### Exercise 1 — Find Maximum Number
Example:
Input:
[4, 7, 1, 9, 3]

Output:
9

### Exercise 2 — Sum of List
Example:
Input:
[1, 2, 3, 4]

Output:
10

---

### Exercise 3 — Remove Duplicates
Example:
Input:
[1, 2, 2, 3, 4, 4]

Output:
[1, 2, 3, 4]

---

### Exercise 4 — Second Largest Number
Example:
Input:
[10, 20, 5, 8]

Output:
10

### Exercise 5 — Linear Search
Example:

Input:
List: [2, 4, 6, 8]
Search: 6

Output:
Element found at index 2

---

# 7️⃣ Mini Challenge
Build a simple To-Do List program.

Features:
- Add task
- View tasks
- Remove task

Example:
1. Add Task
2. View Tasks
3. Remove Task
4. Exit

Hint:
Use:
- lists
- loops
- conditions

---

# ✅ Day 7 Completion Checklist

- [ ] Learned list basics
- [ ] Practiced indexing and slicing
- [ ] Used list methods
- [ ] Solved array problems
- [ ] Completed mini project
- [ ] Pushed code to GitHub
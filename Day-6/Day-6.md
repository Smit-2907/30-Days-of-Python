# 🐍 Day 6 — Strings

## 🎯 Goal
Learn how to work with strings and perform basic string manipulation.

Today you will learn:
- String basics
- String indexing
- String slicing
- Useful string methods

You will also solve **string algorithm problems** to improve logic.

---

# 🗺️ Day 6 Flow (Follow in Order)

### 1️⃣ Creating Strings
A string is a sequence of characters.
Create a file: `string_basics.py`

Example:
```python
name = "John Doe"
message = 'Hello World'
print(name)
print(message)
```

Output:
```
Python
Hello World
```

Explanation:  
Strings can be created using **single quotes** or **double quotes**.

---

### 2️⃣ String Indexing
Strings allow access to individual characters.
Create: `string_indexing.py`

Example:
```python
text = "Python"
print(text[0])
print(text[3])
```

Output:

```
P
h
```

Explanation:  
Python indexing starts from **0**.

---

### 3️⃣ String Slicing
Slicing allows you to extract parts of a string.
Create: `string_slicing.py`

Example:
```python
text = "Python"
print(text[0:3])
print(text[:4])
print(text[2:])
```

Output:
```
Pyt
Pyth
thon
```

Explanation:  
Slicing follows this format:

```
string[start:end]
```

---

### 4️⃣ Useful String Methods
Create: `string_methods.py`

Example:
```python
text = "  hello python  "
print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("python", "world"))
```

Output:
```
  HELLO PYTHON
  hello python
hello python
  hello world
```

Explanation:
- `upper()` → converts to uppercase  
- `lower()` → converts to lowercase  
- `strip()` → removes spaces from beginning and end  
- `replace()` → replaces text  

---

### 5️⃣ Splitting a Sentence
Create: `split_sentence.py`

Example:
```python
sentence = "I love learning Python"
words = sentence.split()
print(words)
```

Output:
```
['I', 'love', 'learning', 'Python']
```

Explanation:  
`split()` converts a sentence into a **list of words**.

---

# 🧠 String Algorithm Exercises

### Exercise 1 — Reverse a String
Hint:
Use slicing.

### Exercise 2 — Palindrome Checker
Hint:
Compare the string with its reverse.

### Exercise 3 — Count Vowels
Write a program that counts vowels in a string.

### Exercise 4 — Find Longest Word
Hint:
Use `split()`.

### Exercise 5 — Character Frequency Counter

Input:
```
banana
```
Output:
```
b : 1
a : 3
n : 2
```

Hint:
Use a dictionary.

---

# 7️⃣ Mini Challenge
Create: `word_frequency_counter.py`
Build a program that counts the frequency of each word in a sentence.

Example:

Input:
```
Python is great and Python is powerful
```
Output:

```
Python : 2
is : 2
great : 1
and : 1
powerful : 1
```

Hint:
Use:
- `split()`
- `dictionary`
- `loops`

---

# ✅ Day 6 Completion Checklist

- [ ] Learned string basics
- [ ] Practiced indexing and slicing
- [ ] Used string methods
- [ ] Solved string algorithm exercises
- [ ] Completed mini challenge
- [ ] Pushed code to GitHub
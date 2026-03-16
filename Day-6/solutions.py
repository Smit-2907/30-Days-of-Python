### Exercise 1 — Reverse a String
print("\nExercise 1 - Reverse a String")
string = input("Enter The String: ")
reversed_string = string[::-1]  # [start:end:step] → step -1 means move backwards, so the string is reversed
print(reversed_string)

### Exercise 2 — Palindrome Checker
print("\nExercise 2 - Palindrome Checker")
text = input("Enter something to check if it is palindrome or not: ")
reversed_text = text[::-1]
if text == reversed_text:
    print("This is Palindrome.")
else:
    print("This is not Palindrome")

### Exercise 3 — Count Vowels
print("\nExercise 3 - Count Vowels")
Input = input("Enter Text to extract the vowels: ")
count= 0
for i in Input:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count += 1
print("This String has", count, "vowels")

### Exercise 4 — Find Longest Word
print("\nFind Longest Word")
STRING = input("Enter Text to find longest word in it: ")
new_string = STRING
words = new_string.split()
longest_word = max(words, key=len)
print("The longest word:", longest_word)

### Exercise 5 — Character Frequency Counter
print("\nExercise 5 - Character Freqency Counter")
string_char = input("Enter the String: ")
char_count = {}
for i in string_char:
    if i in char_count:
        char_count[i] += 1
    else:
        char_count[i] = 1

for char, count in char_count.items():
    print(char, ":", count) 
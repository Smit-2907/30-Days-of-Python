### Exercise 1 — Find Maximum Number
print("\nExercise 1 = Find Maximum Number")
numbers = [2, 5, 7, 9, 3, 1]
max_number = 0 
for num in numbers:
    if num > max_number:
        max_number = num
print("The maximum number is: ", max_number)

### Exercise 2 — Sum of List
print("\nExercise 2 — Sum of List")
sum = 0
for num in numbers:
    sum = sum + num
print("Sum of the list", numbers, "is: ", sum)

### Exercise 3 — Remove Duplicates
print("\nExercise 3 — Remove Duplicates")
elements = [2, 4, 5, 2, 6, 7, 8, 4, 9, 10]
new_elements = []
for num in elements:
    if num not in new_elements:
        new_elements.append(num)
print("Before: ", elements)
print("After: ", new_elements)

### Exercise 4 — Second Largest Number
numbers = [62,3,5,6,34,35,5,6]
largest_number = 0
second_largest_numer = 0
for num in numbers:
    if num > largest_number:
        largest_number = num
for num in numbers:
    if num != largest_number and num > second_largest_numer:
        second_largest_numer = num
        
print("\n Largest number:", largest_number)
print("\n Second Largest number: ", second_largest_numer)

### Exercise 5 — Linear Search
list1 = [2, 4, 5, 1, 9, 5, 7, 3]
key = int(input("Enter the element you want to find index: "))

compare = 0

for num in list1:
    if num == key:
        print(key, "is at index", compare)
    compare += 1
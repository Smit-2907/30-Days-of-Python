# Solution to Exercise 1 — Print Numbers 1 to 20
print("\nExercise 1 -- Print numbers from 1 to 20.")
for i in range(1, 21):
    print(i)

# Solution to Exercise 2 - Even Numbers from 1 to 20
print("\n Exercise 2 -- Print even numbers from 1 to 20.")
for i in range (1, 21):
    if i % 2 ==0:
        print(i)

# Solution to Exercise 3 - Sum of Numbers from 1 to 100
print("\n Exercise 3 -- Sum of numbers from 1 to 100.")
total_sum = 0
for i in range (1, 101):
    total_sum += i
print("The sum of numbers from 1 to 100 is: ", total_sum)
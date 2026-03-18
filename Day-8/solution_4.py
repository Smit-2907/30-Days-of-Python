### Exercise 4 — Maximum Number in List

def max_number():
    numbers = input("Enter elements separated by space: ").split()
    max = 0
    for num in numbers:
        num = int(num) # crusial step if u don't write this it wil not be converted into integer.
        if num > max:
            max = num
    print("The maximum number is: ", max)

max_number()
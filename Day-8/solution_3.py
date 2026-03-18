### Exercise 3 — Sum of List
def sum_list():
    li = input("Enter elements separated by space: ").split()
    sum = 0
    for num in li:
        sum = sum + int(num) # main work is here, this int(num) will convert the string input given by input(), into integer.
    print("The sum of", li, " the list is:", sum)

sum_list()
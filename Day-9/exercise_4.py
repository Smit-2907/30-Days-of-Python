### Exercise 4 — Multiply List using Lambda
# Multiply each element of list by 2.

def multiply_by_2(*numers):
    multipled_numbers = []
    for num in numbers:
        num = int(num)
        num *= num
        multipled_numbers.append(num)
    print("THe multiplied by 2 numbers are: ", multipled_numbers)
    
numbers = input("Enter elements with spaces seperated: ").split()
multiply_by_2(*numbers)

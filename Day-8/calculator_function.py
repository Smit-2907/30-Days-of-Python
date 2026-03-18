#  A simple calculator using functions.
# Features:
# - Add
# - Subtract
# - Multiply
# - Divide

def enter_nums():
    num_1 = int(input("Enter Number 1: "))
    num_2 = int(input("Enter Number 2: "))
    return num_1, num_2
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b

while True:
    print("\n\n1. Addition\n2. Substraction\n3. Multiplicattion\n4. Division\nPress Any Key to Exit\n")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        a, b = enter_nums()
        result = add(a, b)
        print("\nThe Sum is: " ,result)
    elif choice == 2:
        a, b = enter_nums()
        result = sub(a, b)
        print("\n The Substraction is:", result)
    elif choice == 3:
        a, b = enter_nums()
        result = mul(a, b)
        print("The Multiplication is: ", result)
    elif choice == 4:
        a, b = enter_nums()
        result = div(a, b)
        print("The Division is: ", result)
    else:
        exit()


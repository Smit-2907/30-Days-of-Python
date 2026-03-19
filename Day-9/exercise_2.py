# Find the maximum number from given inputs.
def find_max(*number):
    max_num = 0
    for num in number:
        num = int(num)
        if num > max_num:
            max_num = num
    print("max number is:", max_num)

numbers = input("enter numbers with spaces: ").split()
find_max(*numbers)
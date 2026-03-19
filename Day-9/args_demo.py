def add_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    print(total)
add_numbers(1, 2, 3, 4, 5)
### Exercise 5 — Check Prime Number
def check_prime():
    num = int(input("Enter number to check whether it is prime or not: "))
    for i in range(2, num):
        if num % i == 0:
            print("The current number is not a prime number.")
            break
        else:
            print("The current number is a prime number.")
            break
check_prime()
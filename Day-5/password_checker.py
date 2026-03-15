# This program checks if the entered password is correct or not until the correct password is entered.
correct_paaword = "admin@123"
while True:
    password = input("Enter the password: ")
    if password == correct_paaword:
        print("Access Granted")
        break
    else:
        print("Access Denied. Try Again.")
# This is a simple grade checker program that takes the marks as input and checks the grade using "if-elif-else" statement.
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Your grade is A.")
elif marks >= 75:
    print("Your grade is B.")
elif marks >= 60:
    print("Your grade is C.")
else:
    print("Your grade is D")

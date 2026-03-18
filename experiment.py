import webbrowser
import time

correct_number = 69
max_attempts = 3
count = 0

def show_cat(win=True):
    if win:
        print(r"""
 /\_/\  
( o.o )  YOU DID IT!!!
> ^ <
        """)
    else:
        print(r"""
 /\_/\  
( T_T )  YOU LOST...
> ^ <
        """)

print("Welcome to Guess The Number Game!")
print(f"You have {max_attempts} attempts.\n")

while count < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number.\n")
        continue

    if guess == correct_number:
        print("\nCongratulations! You guessed it right!")

        show_cat(win=True)

        print("\nPlaying your reward...")
        time.sleep(1)

        # Rickroll
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

        break

    elif guess < correct_number:
        print("Too low!\n")
    else:
        print("Too high!\n")

    count += 1
    print(f"Attempts left: {max_attempts - count}\n")

else:
    print("\nGame Over. You lost!")

    show_cat(win=False)

    print("\nPlaying sad vibes...")
    time.sleep(1)

    webbrowser.open("https://youtube.com/shorts/Zggn8Ad_AuQ?si=Ogxu5XvWtFbB5795")

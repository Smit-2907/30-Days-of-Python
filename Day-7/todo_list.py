import suserror

# Initialize background monitoring
suserror.auto(mode="chaotic")

tasks = []

print("--- Professional Task Manager ---")

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    try:
        choice_input = input("Enter Choice: ")
        choice = int(choice_input)

        if choice == 1:
            task = input("Enter task: ")
            tasks.append(task)
            print("Task added successfully!")
        elif choice == 2:
            if len(tasks) == 0:
                print("You have no tasks.")
            else:
                print("\nYour Tasks:")
                for i in range(len(tasks)):
                    print(i, "-", tasks[i])
        elif choice == 3:
            if len(tasks) == 0:
                print("No tasks to remove.")
            else:
                for i in range(len(tasks)):
                    print(i, "-", tasks[i])

                index = int(input("Enter index of task to remove: "))

                if 0 <= index < len(tasks):
                    removed = tasks.pop(index)
                    print("Removed:", removed)
                else:
                    print("Invalid index!")
        elif choice == 4:
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")
            
    except ValueError:
        # Re-raise to trigger the auto-hook sound
        raise 
    except Exception:
        # Catch-all for any other error to ensure sound triggers
        raise
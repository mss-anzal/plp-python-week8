
# Personal Mini-Toolkit - Week 8 Final Project

# Store tasks while the program is running
tasks = []

# Welcome message
print("================================")
print("     PERSONAL MINI-TOOLKIT")
print("================================")
print("Welcome! This toolkit has three useful tools.")

# Main menu loop
while True:
    print("\n===== MAIN MENU =====")
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Number Guessing Game")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    # Tool 1: Simple Calculator
    if choice == "1":
        print("\n--- SIMPLE CALCULATOR ---")

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        print("\nChoose an operation:")
        print("+ Addition")
        print("- Subtraction")
        print("* Multiplication")
        print("/ Division")

        operation = input("Enter operation: ")

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Sorry, division by zero is not allowed.")
                continue
        else:
            print("Invalid operation. Please try again.")
            continue

        print(f"The answer is: {result}")

    # Tool 2: To-Do List
    elif choice == "2":
        print("\n--- TO-DO LIST ---")

        while True:
            print("\n1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Return to main menu")

            task_choice = input("Choose an option: ")

            if task_choice == "1":
                new_task = input("Enter your task: ").strip()

                if new_task:
                    tasks.append(new_task)
                    print(f"Task '{new_task}' added successfully!")
                else:
                    print("Task cannot be empty.")

            elif task_choice == "2":
                if len(tasks) == 0:
                    print("Your to-do list is empty.")
                else:
                    print("\nYour tasks:")
                    for index, task in enumerate(tasks, start=1):
                        print(f"{index}. {task}")

            elif task_choice == "3":
                if len(tasks) == 0:
                    print("There are no tasks to remove.")
                else:
                    print("\nYour tasks:")
                    for index, task in enumerate(tasks, start=1):
                        print(f"{index}. {task}")

                    try:
                        task_number = int(input("Enter task number to remove: "))

                        if 1 <= task_number <= len(tasks):
                            removed_task = tasks.pop(task_number - 1)
                            print(f"Task '{removed_task}' removed successfully!")
                        else:
                            print("Invalid task number.")
                    except ValueError:
                        print("Please enter a valid whole number.")

            elif task_choice == "4":
                print("Returning to the main menu...")
                break

            else:
                print("Invalid option. Please try again.")

    # Tool 3: Number Guessing Game
    elif choice == "3":
        # Generate a secret number between 1 and 10
        import random

        secret_number = random.randint(1, 10)
        attempts = 0

        print("\n--- NUMBER GUESSING GAME ---")
        print("I have chosen a number between 1 and 10.")
        print("Can you guess it?")

        while True:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Please enter a whole number.")
                continue

            attempts += 1

            if guess < 1 or guess > 10:
                print("Please choose a number between 1 and 10.")
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You guessed the number {secret_number}!")
                print(f"You used {attempts} attempts.")
                break

    # Quit the program
    elif choice == "4":
        print("\nThank you for using the Personal Mini-Toolkit!")
        print("Goodbye! Keep learning Python.")
        break

    # Handle invalid menu choices
    else:
        print(f"Sorry, '{choice}' is not a valid choice. Please try again.")

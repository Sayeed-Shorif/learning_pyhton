"""1. To-Do List Application

Description:
Create a simple to-do list application in Python. This project will teach you
the basics of working with lists, user input, and simple command-line interfaces.

Project Requirements:

Allow the user to add tasks to the to-do list.
Allow the user to mark tasks as completed and remove completed tasks.
Display the to-do list to the user.
Implementation:
You can use Python's built-in data structures like lists or dictionaries to
manage the to-do list. Implement a menu-driven interface using functions
and loops to add, mark, and remove tasks. You can use simple print statements to display
the list to the user."""
# implementing the main list
to_do_list = []
# creating a function to add task in the list
def add(n):
    for i in range(n):
        new = input(f"Enter the name of task {i + 1} :")
        to_do_list.append(new)
    return print(f"Successfully added {n} tasks.")
def mark(num):
    to_do_list.pop(num - 1)
    return to_do_list

while True:
    print("\nMain Menu : \n")
    print("Here are the module you can use :")
    print("1. Add task to your to-do list.")
    print("2. Mark and remove a task.")
    print("3. Display your to do list.")
    print("4. To exit the programme.")

    choice = int(input("Enter the number of the module you want to perform : "))
    if choice == 1:
        n = int(input("Enter the number of task you want to add : "))
        if n <= 0:
            print("Enter a valid number !")
        else:
            add(n)
    elif choice == 2 :
        if len(to_do_list) == 0:
            print("Your to-do list is empty first add some task to your to-do list then perform this module !")
        else:
            number = 0
            print("Here is your to-do list :")
            for i in to_do_list:
                number += 1
                print(f" {number} : {i}")
            num = int(input("Enter the number of task you want to mark and remove it ."))
            print(f" {num} no task has been marked and \nthe task has been removed here is the new to do list :  ")
            n = 0
            for _ in mark(num):
                n += 1
                print(f"{n} : {_}")
    elif choice == 3:
        print("Here is your to-do list : ")
        num = 0
        for _ in to_do_list:
            num += 1
            print(f"{num} : {_}")
    elif choice == 4:
        print("thank you for using this code!")
        break
    else:
        print("Baka enter the right number !")





"""2. Number Guessing Game

Description:
Build a number guessing game in Python where the computer selects a random number, 
and the player has to guess it. This project will introduce you to random number generation, user input validation, and conditional statements.

Project Requirements:

Generate a random number between a specified range (e.g., 1 to 100).
Allow the player to guess the number.
Provide hints (e.g., "Too high" or "Too low") until the player guesses correctly.
Keep track of the number of attempts and display it when the player guesses correctly.
Implementation:
You can use the random module to generate a random number within the specified range. 
Implement a loop to repeatedly ask the player for their guess, 
compare it to the random number, and provide feedback. 
Use a variable to keep track of the number of attempts."""
# Number guessing project
import random
secret_number = random.randint(1,100)
print("Welcome to a number guessing game !")
print("Let's see how many attempts do you need to guess the right number.")
attemts = 0
print("The number is between 1 to 100 :")
while True:
    guess = int(input("Enter your guess :"))
    attemts += 1
    if guess > secret_number:
        print("Too high .")
    elif guess < secret_number:
        print("Too low .")
    elif guess == secret_number:
        print(f"Congratulations! You have successfully guessed the secret number: {secret_number} in {attemts} attempts.")
        break
    else:
        print("Enter a valid number !")


"""3. Simple Calculator

Description:
Develop a basic calculator in Python that can perform arithmetic operations 
like addition, subtraction, multiplication, and division. 
This project will help you understand user-defined functions and conditional statements.

Project Requirements:

Take two numbers and an operator as input from the user.
Perform the selected operation and display the result.
Handle invalid inputs, such as division by zero or unsupported operators.
Allow the user to perform multiple calculations in a single session.
Implementation:
Create functions for each operation (e.g., add, subtract, multiply, divide) and
call them based on the operator input. Use conditionals to handle
edge cases like division by zero. Implement a loop to allow the user 
to continue making calculations until they choose to exit."""

print("Welcome to  a arithmatic calculator made by Sayeed Shorif.")
# creating function for calculation
# func for addition
def add(a,b):
    return a + b
# func for subtraction
def sub(a,b):
    if a == b:
        return 0
    else:
        return a - b


# func for multiplication.
def mul(a,b):
    return a * b
#func for division.
def div(a,b):
    if a == 0:
        return 0
    elif b == 0:
        return "Math Error !"
    else:
        return a / b
def user_input():
    a = int(input("Enter the first number :"))
    b = int(input("Enter the second number :"))
    return a,b

print("ARITHMATIC CALCULATOR\n")
print("Menu :")
print("1.Addition of two numbers.")
print("2.Subtraction of two numbers.")
print("3.Multiplication of two numbers.")
print("4.Division of two numbers.")
print("5.Exit.")
while True:
    user = int(input("Enter a calculation number to perfom the calculation :"))
    if user == 1:
        print(f"Here is the Addition of {a} and {b} is :{add(a,b)}")
    elif user == 2:
        a = int(input("Enter the first number :"))
        b = int(input("Enter the second number :"))
        print(f"Here is the Subtraction of {a} and {b} is :{sub(a, b)}")
    elif user == 3:
        a = int(input("Enter the first number :"))
        b = int(input("Enter the second number :"))
        print(f"Here is the Multipication {a} and {b} is :{mul(a, b)}")
    elif user == 4:
        a = int(input("Enter the first number :"))
        b = int(input("Enter the second number :"))
        print(f"Here is the Division of {a} and {b} is :{div(a, b)}")
    elif user == 5:
        print("You choose to exit the calculator .\nThank  you for using this calculator.")
        break
    else:
        print("Enter a valid number !")



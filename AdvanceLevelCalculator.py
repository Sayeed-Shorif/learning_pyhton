# project description :
"""In this project I will create a simple python calculator which will perform addition ,Subtraction
division , multiplication ,factorial,square,square root.
"""
# cheak user input
def cheakUserinput():
    while True:
        a = input("Enter The First Number : ")
        try:
            a = int(a)
            break
        except:
            print("INVALID!!!.\nEnter a valid number.")
    while True:
        b = input("Enter The Second Number : ")
        try:
            b = int(b)
            break
        except:
            print("INVALID!!!.\nEnter a valid number.")
    return a,b
def factorial():
    while True:
        n = input("Enter the number : ")
        try:
            n = int(n)
            break
        except:
            print("INVALID!!!\nEnter a valid number.")
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

def squre():
    while True:
        n = input("Enter the number : ")
        try:
            n = int(n)
            break
        except:
            print("INVALID!!!\nEnter a valid number.")
    return n*n
import math
def squreRoot():
    while True:
        n = input("Enter the number : ")
        try:
            n = int(n)
            break
        except:
            print("INVALID!!!\nEnter a valid number.")
    return math.sqrt(n)
# the body of the calculator.
print("Project Calculator.")
print("Available Modules :")
print("1.Addition.(add two numbers.)")
print("2.Subtraction.(subtract a number from another number.)")
print("3.Multiplication.(multiplication of two numbers.)")
print("4.Division.(Divide a number by another number.)")
print("5.Factorial.(Return the factorial of the input number.)")
print("6.Square.(Return the squared value of the number.)")
print("7.SquareRoot.(Return the squareRoot value of the number.)")
print("8.Exit the calculator.")
while True:
    while True:
        user_input = input("Enter the number of a module you want to perform : ")
        try:
            user_input = int(user_input)
            if 1 <= user_input < 9:
                break
            else:
                print("An error occurred. Enter a number between 1 to 8")
        except:
            print("INVALID!!!.\nEnter a valid number.")
    if user_input == 1:
        print("You choose to Additon.")
        a,b = cheakUserinput()
        ans = lambda a, b : a + b
        print(f"The Addition of {a} and {b} is :", ans(a,b))
    elif user_input == 2:
        print("You choose to Subtraction.")
        a,b = cheakUserinput()
        ans = lambda a, b : a - b
        print(f"The Subtraction of {a} and {b} is :", ans(a,b))
    elif user_input == 3:
        print("You choose to Multiplication.")
        a,b = cheakUserinput()
        ans = lambda a, b: a * b
        print(f"The Multiplication of {a} and {b} is :", ans(a, b))
    elif user_input == 4:
        print("You choose to Division.")
        a, b = cheakUserinput()
        ans = lambda a, b: a / b
        print(f"The Division of {a} and {b} is :", ans(a, b))
    elif user_input == 5:
        print("You choose to do factorial.")
        ans = factorial()
        print(f"The factorial is : {ans}")
    elif user_input == 6:
        print("You choose to do Square.")
        print(f"The squared value is : {squre()}")
    elif user_input == 7:
        print("You choose to SquareRoot.")
        print(f"The squareRoot value is : {squreRoot()}")
    else:
        print("You choose to Exit.")
        break

import time
time.sleep(1)
print("Thank you for using my calculator.")
time.sleep(1)
print("Made by Sayeed Shorif.")










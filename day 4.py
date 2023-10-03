# For Loop Practice:
#
# Write a Python program that prints all the numbers from 1 to 10.
for i in range(1,11):
    print(i)
# Write a Python program that calculates the sum of all the numbers from 1 to 100.
total = 0
for j in range(1,101):
    total += j
print(total)
# Write a Python program that prints the even numbers from 1 to 20.
for k in range(1,21):
    if k % 2 == 0:
        print(k)
# Write a Python program that prints the first 10 multiples of 5.
given_number = int(input("enter a number : "))
total2 = 0
for s in range(1,given_number+1):
    total2 = given_number * s
    print(f"the mul of {given_number} and {s} is : ",total2)
# Write a Python program that prints the Fibonacci sequence up to the 10th term.
terms = int(input("enter  a number : "))
a = 0
b = 1
fib = 0
for i in range(terms):
    print(fib)
    a = b
    b = fib
    fib = a + b

# While Loop Practice:
#
# Write a Python program that counts from 1 to 10 using a while loop.
a = 1
while a <=10:
    print(a)
    a += 1

# Write a Python program that calculates the factorial of a given number using a while loop.
n = int(input("enter a number to calculate the factorial value : "))
total = 1
while n > 0:
    total = n * total
    n -= 1
print(total)
# Write a Python program that checks if a number is prime using a while loop.
while True:
    input_number = int(input("Enter a number to check if prime: "))
    if input_number > 1:
        prime_number = True
        for i in range(2, input_number):  # Start from 2 and go up to (input_number - 1)
            if input_number % i == 0:
                prime_number = False
                break  # Break out of the loop as soon as a divisor is found
        if prime_number:
            print(input_number, "is a prime number.")
        else:
            print(input_number, "is not a prime number.")
    else:
        print("Please enter a number greater than 1.")
    break


# Write a Python program that prints a countdown from 10 to 1 using a while loop.
import time
num = 10
while num > 0:
    print(num)
    num -= 1
    time.sleep(1)
print("finished")
# Write a Python program that simulates a simple guessing game.
# Generate a random number between 1 and 100,
# and have the user guess the number.
# Provide feedback on whether the guess is too high or too low,
# and continue until the user guesses correctly.
import random
secret_number = random.randint(1,100)
attempts = 0
while True:
    guess = int(input("guess the number between 1 to 100 : "))
    attempts += 1
    if guess == secret_number:
        print(f"congratulations you guessed the right number in {attempts} attempts ")
        break
    elif guess > secret_number:
        print("you are too high !")
    else:
        print("you are too low !")




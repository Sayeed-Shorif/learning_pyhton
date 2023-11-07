from menu import *
import time
print("Welcome to coffee maker.")
a.items()
while True:
    user_choice = int(input("Enter your choice : "))

    choice = a.select(user_choice)
    if choice == "americano":
        coins = int(input("Enter your coin : "))
        if coins > 4:
            print(f'''
                         )))
                        (((
                      +-----+
                      |     |] - Here's your Americano. Enjoy! :)
                      `-----'
                    ''')
            print(f"here is your change : {coins - 4} $")
            time.sleep(3)
        elif coins == 4:
            print(f'''
                         )))
                        (((
                      +-----+
                      |     |] - Here's your Americano. Enjoy! :)
                      `-----'
                    ''')
            time.sleep(3)
        else:
            print("Not enough money.")
    elif choice == "cappuccino":
        coins = int(input("Enter your coin : "))
        if coins > 3:
            print(f'''
                         )))
                        (((
                      +-----+
                      |     |] - Here's your Cappuccino. Enjoy! :)
                      `-----'
                    ''')
            print(f"here is your change : {coins - 3} $")
            time.sleep(3)
        elif coins == 3:
            print(f'''
                         )))
                        (((
                      +-----+
                      |     |] - Here's your Cappuccino. Enjoy! :)
                      `-----'
                    ''')
            time.sleep(3)
        else:
            print("Not enough money.")
    elif choice == "espresso":
        coins = int(input("Enter your coin : "))
        if coins > 2:
            print(f'''
                         )))
                        (((
                      +-----+
                      |     |] - Here's your Espresso. Enjoy! :)
                      `-----'
                    ''')
            print(f"here is your change : {coins - 2} $")
            time.sleep(3)
        elif coins == 2:
            print(f'''
                         )))
                        (((
                      +-----+
                      |     |] - Here's your Espresso. Enjoy! :)
                      `-----'
                    ''')
            time.sleep(3)
        else:
            print("Not enough money.")
    elif choice == "exit":
        print("You choose to exits .")
        break
    else:
        print("Enter a valid Number.")
print("Thank You for using this Project.")
time.sleep(2)
print('\033[31mMade by : Sayeed Shorif.\033[m')







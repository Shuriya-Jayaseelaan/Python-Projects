# Import from Random Library
from random import randint

# Define Functions
def menu():
    print("Welcome to NumGame!\n")
    print("1. Start Game")
    print("2. Exit\n")

def start():
    print("\nIm thinking of a number between 1 and 10\n")
    
    # Generate a random number
    rand_num = randint(1, 10)
    
    # Ask for User Input
    user_num = int(input("Enter the number: "))
    
    # Loops Until User Gets It
    while user_num != rand_num:
        
        if user_num < rand_num:
            print("\nToo Low\n")
    
        elif user_num > rand_num:
            print("\nToo High\n")
    
        user_num = int(input("Try again: "))
    
    print("\nCongrats! You guessed it!")

# Call Menu Function
menu()

user_option = int(input("Enter your option: "))

if user_option == 1:
    # Call Start Function
    start()

else:
    exit()

print("\nSee you again!\n")
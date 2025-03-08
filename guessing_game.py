import random
from colorama import init, Fore, Back, Style

random_number = random.randint(1,20) # Generates a random integer 1 - 20

print("Guess a number 1-20. You have 5 attempts.")
print(f"The number is, {random_number}") # Used for Debugging

number_of_tries = 1 # User guess starts with a base value of 1

user_guess = int(input("Guess: ")) 

while user_guess != random_number and number_of_tries <= 4: # Loops until either of the conditions run as False
        try:
            
            if user_guess > random_number: 
                print("too high")
            
            else: # if user input is too high or low, it will let them know
                 print("too low")

            
            user_guess = int(input("Try again: ")) # prompts the user to try again
            number_of_tries += 1 # Adds 1 to each attempt 
        except ValueError:
             print("Input a number")
if user_guess == random_number:
    print()
    print(f"You Guessed the Number! {random_number}")
    print()
    print(f"It took you {number_of_tries} attempt(s).") # When the user guesses the number, a winning message and number of attempts displays
    print()

else:
    print(f"You took to many attempts. The number was, {random_number}") # If the loop fails due to number_of_tries <= 4, this message displays

 


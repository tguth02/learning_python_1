import random

random_number = random.randint(1,20) # Generates a random integer 1 - 20

print("Guess a number 1-20. You have 5 attempts.")
# print(f"The number is {random_number}") # Used for Debugging

number_of_tries = 1 # User guess starts with a base value of 1

user_guess = int(input("Guess: ")) 

while user_guess != random_number and number_of_tries <= 4: # Loops until either of the conditions run as False
        try:
            
            if user_guess > random_number: 
                print("\033[31mtoo high\033[0m")
            
            else: # if user input is too high or low, it will let them know
                 print("\033[31mtoo low\033[0m")

            user_guess = int(input("Try again: ")) # prompts the user to try again
            number_of_tries += 1 # Adds 1 to each attempt 
        
        except ValueError:
             print("Input a number")
if user_guess == random_number:
    print(f"\n \033[32mYou Guessed the Number! {random_number}\033[0m")
    print(f"\n It took you {number_of_tries} attempt(s).\n") # When the user guesses the number, a winning message and number of attempts displays

else:
    print(f"\033[31mYou took to many attempts. The number was, {random_number}\033[0m") # If the loop fails due to number_of_tries <= 4, this message displays
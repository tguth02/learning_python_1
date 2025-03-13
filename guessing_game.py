import random
from colorama import init, Fore, Back, Style

init(autoreset=True)

random_number = random.randint(1,20) # Generates a random integer 1 - 20

print("Guess a number 1-20. You have 5 attempts.")
print(f"The number is {random_number}") # Used for Debugging

number_of_tries = 0 # User guess starts with a base value of 1

user_guess = int(input("Guess: ")) 

number_of_tries += 1

while user_guess != random_number and number_of_tries < 5: # Loops until either of the conditions run as False
        try:
            # print(f"before {number_of_tries}")
            if user_guess > random_number: 
                print(Fore.CYAN + "Too High")
            else: # if user input is too high or low, it will let them know
                 print(Fore.CYAN + "Too Low")

            user_guess = int(input("Try again: ")) # prompts the user to try again
            number_of_tries += 1 # Adds 1 to each attempt 
            # print(f"after {number_of_tries}")
        except ValueError:
             print("Input a number")
if user_guess == random_number:
    print(Fore.GREEN + f"\n You Guessed the Number! {str(random_number)}")
    print(f"\n It took you {number_of_tries} attempt(s).\n") # When the user guesses the number, a winning message and number of attempts displays
else:
    print(Fore.RED + f"You took too many attempts. The number was, {random_number}") # If the loop ends due to number_of_tries <= 4, this message displays
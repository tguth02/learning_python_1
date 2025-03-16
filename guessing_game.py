import random
from colorama import init, Fore, Back, Style

init(autoreset=True)

def the_game():
    random_number = random.randint(1,20) # Generates a random integer 1 - 20

    print("Guess a number 1-20. You have 5 attempts.")
    # print(f"The number is {random_number}") # Used for Debugging
    
    user_guess = None
    number_of_tries = 0
    
    
    while user_guess != random_number and number_of_tries < 5: # Loops until either of the conditions run as False
        try:
            if number_of_tries == 0:
                user_guess = int(input("Guess: ")) # Prompts user input
                number_of_tries += 1  # Adds 1 to each attempt   
            else:
                if user_guess > random_number: 
                    print(Fore.CYAN + "Too High") # Added color to text to be easier to read
                else: # if user input is too high or low, it will let them know
                    print(Fore.CYAN + "Too Low")
                user_guess = int(input("Try again: "))
                number_of_tries += 1     
        except ValueError:
            print("Input a number")
    if user_guess == random_number:
        print(Fore.GREEN + f"\n You Guessed the Number! {str(random_number)}")
        print(f"\n It took you {number_of_tries} attempt(s).\n") # When the user guesses the number, a winning message and number of attempts displays
    else:
        print(Fore.RED + f"You took too many attempts. The number was, {random_number}") # If the loop ends due to number_of_tries <= 4, this message displays

the_game() # The function runs





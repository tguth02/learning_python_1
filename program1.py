

print("Welcome to the bar. What is your age?")

try:
    my_age = int(input("Your Age: ")) # Change user input into an integer
    if my_age >= 21: # Verifying user input is >= 21
            print("Have a drink.")
    else:
            print("You are not old enough.")
except ValueError: # If ValueError occurs, display this message
       print("Please enter a number.")
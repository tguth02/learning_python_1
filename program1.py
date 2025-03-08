

print("Welcome to the bar. What is your age?")

while ValueError: # Creates a loop if conditional is True
        try:
                age = int(input("Your Age: ")) # Change user input into an integer
                if age >= 21: # Verifying user input is >= 21
                        print("Have a drink.")
                else:
                        print("You are not old enough.")
                break # Executes code
        except ValueError: # If ValueError occurs, display this message
                print("Please enter a number.")

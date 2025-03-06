from utils import convert_age_to_int

print("Welcome to the bar. What is your age?")

my_age = input("Your Age: ")

my_age_in_integer = convert_age_to_int(my_age) 

# Check if older than 21
if my_age_in_integer >= 21:
    print("Have a drink.")
else:
    print("You are not old enough.")
import random
from colorama import init, Fore, Back, Style
from flip_images import heads_img, tails_img, win_img, lose_img

init(autoreset=True) # Initializing colorama 


# Collect user prediction and sanitize it
user_prediction = input("Which side do you think the coin will land?: ")
user_prediction = user_prediction.lower() # Sanitizing user input to be all lowercase

# Generate random float between 0-1 to convert to heads or tails
random_float = random.random()
result = "" # An empty string to store the result of the coin toss (heads or tails)

# Convert float to heads or tails result
if random_float < 0.5:
    result = "heads"
else: 
    result = "tails"

# Print result (both ASCII image and sentence)
if result == "heads":
    print(Fore.BLUE + heads_img)
elif result == "tails":
    print(Fore.BLUE + tails_img)

print(f"The result was {Fore.BLUE + result}.")

# Check if user prediction is valid and is wrong or right
if user_prediction == "heads" or user_prediction == "tails":
    if user_prediction == result:
        print(Fore.GREEN + win_img)
    else:
        print(Fore.RED + lose_img)
else:
    print("Incorrect Input.")
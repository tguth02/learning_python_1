import random 

print("Make your choices to build your dish!") # Comment number 2

def pasta_build(): # Function for the user to choose a pasta dish 
  sauces = ["Red sauce", "Meat sauce", "Vodka sauce", "Alfredo sauce"]
  meat  = ["Chicken", "Italian Sausage", "Ground Beef"]   # The different choices that the user can pick 
  pasta = ["Penne", "Fettuccine", "Linguine", "Rigatoni"]

  type_sauce = input("\nWhat type of sauce do you want?: \n")

  type_meat =  input("\nWhat type of meat do you want?: \n")

  type_pasta =  input("\nWhat type of pasta do you want?: \n") 

  print(type_sauce + " " + type_pasta + " " + type_meat) # Creates the dish that the user creates 

pasta_build() # Runs the program




import random 

print("Make your choices to build your dish!")

def pasta_build():
  sauces = ["Red sauce", "Meat sauce", "Vodka sauce", "Alfredo sauce"]
  meat  = ["Chicken", "Italian Sausage", "Ground Beef"]
  pasta = ["Penne", "Fettuccine", "Linguine", "Rigatoni"]

  type_sauce = input("\nWhat type of sauce do you want?: \n")

  type_meat =  input("\nWhat type of meat do you want?: \n")

  type_pasta =  input("\nWhat type of pasta do you want?: \n")

  print(type_sauce + " " + type_pasta + " " + type_meat)

pasta_build()




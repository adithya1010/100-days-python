#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
letters_in_password=""
for i in range(0,nr_letters):
  random_letter=random.choice(letters)
  letters_in_password=letters_in_password+random_letter

symbols_in_password=""
for i in range(0,nr_symbols):
  random_symbol=random.choice(symbols)
  symbols_in_password=symbols_in_password+random_symbol

numbers_in_password=""
for i in range(0,nr_numbers):
  random_number=random.choice(numbers)
  numbers_in_password=numbers_in_password+random_number

password=letters_in_password+symbols_in_password+numbers_in_password

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list=[]
for i in range(0,nr_letters):
  password_list.append(random.choice(letters))

for i in range(0,nr_symbols):
  password_list.append(random.choice(symbols))

for i in range(0,nr_numbers):
  password_list.append(random.choice(numbers))

random.shuffle(password_list)
final_shuffled_password=""
for i in password_list:
  final_shuffled_password=final_shuffled_password+i

print(final_shuffled_password)




#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

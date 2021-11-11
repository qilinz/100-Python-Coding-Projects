# Password Generator Project
# import packages
import random

# generate lists for letters, numbers and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# greetings and requirements from users
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
if nr_letters > 0:
    for letter in range(0, nr_letters):
        password += letters[random.randint(0, len(letters) - 1)]
        # A easier way using random module: password += random.choice(symbols)
if nr_symbols > 0:
    for symbol in range(0, nr_symbols):
        password += symbols[random.randint(0, len(symbols) - 1)]
if nr_numbers > 0:
    for number in range(0, nr_numbers):
        password += numbers[random.randint(0, len(numbers) - 1)]
print(f"Your easy password is: {password}")

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
''' 
How I tackle this issue: 
random get one character from the password generated above and then remove it.
'''
# get a copy
password_copy = password
hard_password = ""
# find the password length
nr_password = len(password)

# generate the hard password
for char in range(0, nr_password):
    # (1) get a random character from the password of the easy level
    random_char = password_copy[random.randint(0, len(password_copy) - 1)]
    # (2) add it to the hard_password
    hard_password += random_char
    # (3) remove the added character. Attention: only replace ONE.
    password_copy = password_copy.replace(random_char, "", 1)
print(f"Your hard password is: {hard_password}")

'''
Other ways to code the hard password:
(1) using random.shuffle(). This can be used to randomly shuffle elements of list. CANNOT be used for str and tuple.

    random.shuffle(password_list)
    hard_password = ""
    for char in password_list:
        hard_password += char
    print(hard_password)
    
(2) generate a new order of the index, then get the list using it.

    my_list = ['a', 'b', 'c', 'd', 'e']
    my_order = [3, 2, 0, 1, 4]
    my_list = [my_list[i] for i in my_order]
    print(my_list) 
    
    Source: https://stackoverflow.com/questions/2177590/how-can-i-reorder-a-list/2177607
    Source explaining [my_list[i] for i in my_order] (List Comprehensions): https://realpython.com/list-comprehension-python/#using-list-comprehensions
'''
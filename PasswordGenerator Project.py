import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level: sequence of letter, numbers, and symbols
password = ""
for char in range(nr_letters):
    random_char = random.choice(letters)
    password += random_char
for i in range(nr_numbers):
    random_num = random.choice(numbers)
    password += random_num
for sym in range(nr_symbols):
    random_sym = random.choice(symbols)
    password += random_sym
print(password)

# Hard Level: randomized
password_list = []
for char in range(nr_letters):
    random_char = random.choice(letters)
    password_list.append(random_char)
for i in range(nr_numbers):
    random_num = random.choice(numbers)
    password_list.append(random_num)
for sym in range(nr_symbols):
    random_sym = random.choice(symbols)
    password_list.append(random_sym)
print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your password is {password}")

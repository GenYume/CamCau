import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pass_caracs = []

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for l in range(1, nr_letters+1) :
    pass_caracs.append(letters[random.randint(0,len(letters)-1)])
for s in range(1, nr_symbols+1) :
    pass_caracs.append(symbols[random.randint(0,len(symbols)-1)])
for n in range(1, nr_numbers+1) :
    pass_caracs.append(numbers[random.randint(0,len(numbers)-1)])

password = ""
for p in range(0, len(pass_caracs)):
    password += pass_caracs[p]

print(pass_caracs)
print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hard_password = ""
random_pass_caracs = pass_caracs[:]
random.shuffle(random_pass_caracs)
for h in range(0, len(random_pass_caracs)):
    hard_password += random_pass_caracs[h]

print(random_pass_caracs)
print(hard_password)

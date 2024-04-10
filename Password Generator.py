import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True): 
    #function with bydefault arguments
    characters = '' #empty String
    if use_letters:
        characters += string.ascii_letters #adds all the alphabets(big and small)
    if use_numbers:
        characters += string.digits #adds all the digits to string "characters"
    if use_symbols:
        characters += string.punctuation #adds all the symbols to the string "characters"

    if len(characters) == 0:
        print("Error: At least one character type should be selected.")
        return None

    password = ''.join(random.choice(characters) for i in range(length))
    return password

print("Welcome to the Password Generator!")
length = int(input("Enter desired password length: "))
use_letters = input("Include letters? (yes/no): ").lower() == 'yes'  #returns True or False
use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'
password = generate_password(length, use_letters, use_numbers, use_symbols)
if password:
    print("Generated Password:", password)

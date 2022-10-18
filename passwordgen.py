# ask user do they want a generated password?
# if yes then generate password, after asking for the length required
# generate and print new password
# if initial response is no then exit the program

import string
import random 

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(input("How long would you like your password to be? "))
    
    random.shuffle(characters)

    password = []
    #"".join(characters[:password_length])

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)

option = input("Do you want to generate a password? (Y/N): ")

if option == "y":
    generate_password()
elif option == "n":
    print("Goodbye Cruel World")
    quit()
else: 
    print("Invalid input, choose Y or N")
    quit()
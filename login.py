

user = input ("Enter your name: ")
print('Welcome to this CLI ' + user)

option = int(input("Would you like to: \n 1. Sign up \n 2. Login \n"))

if option == 1:
    username = input("Choose a username: ")
    password = input("Choose a password: ")

if option == 2:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

else:
    print("Not available.")
    

 


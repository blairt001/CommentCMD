from user import User

def login():
    user = input ("Enter your name: ")
    print('Welcome to this CLI ' + user)
    
    option = int(input("Would you like to: \n 1. Sign up \n 2. Login \n"))
    
    if option == 1:
        user = User().create_user()

    if option == 2:
        user = User().login_user()

    else:
        print("Not available.")
    

 


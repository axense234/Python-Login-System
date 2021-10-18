from Account2 import saved_email
from Account2 import saved_username
from Account2 import saved_password
account_existence = input("Hello,do you have an account? ")
if account_existence.lower() not in "yesno":
    print("Please type Yes if you agree or No if you do not agree next time!")
if account_existence.lower() in "no" and account_existence.lower().endswith("no"):
    account_m_process = input("Do you want to make an account? ")
    if account_m_process.lower() in "yes" and account_existence.lower().endswith("yes"):
        print("Please enter your email,username and password: ")
        email = input("Email: ")
        if not email.endswith("@gmail.com"):
            print("Invalid email!")
        else:
            saved_email = email
            saved_username = input("Username: ")
            saved_password = input("Password: ")
            Account2_file = open("Account2.py", "w")
            Account2_file.write("saved_email = " "\"" + saved_email + "\"" "\n")
            Account2_file.write("saved_username = " "\"" + saved_username + "\"" "\n")
            Account2_file.write("saved_password = " "\"" + saved_password + "\"")
            Account2_file.close()
            print("Congratulations on the birth of your account!")
    elif account_m_process.lower() in "no":
        print("Ok!")
    elif account_m_process.lower() not in "yesno":
        print("Please type Yes if you agree or No if you do not agree next time!")
elif account_existence.lower() in "yes":
    print("Please enter your email,username and password: ")
    email = input("Email: ")
    username = input("Username: ")
    password = input("Password: ")
    if email == saved_email and username == saved_username and password == saved_password:
        print("Welcome back " + saved_username + "!")
    elif email != saved_email:
        print("Invalid email!")
    elif username == saved_username and not password == saved_password:
        password_verification = input("Wrong password,try again? ")
        if password_verification.lower() in "yes":
            tries_password = 5
            while tries_password > 0:
                password = input("Password: ")
                tries_password -= 1
                if password == saved_password:
                    print("Welcome back!")
                elif password != saved_password and not tries_password == 1:
                    print("Wrong password!")
                elif tries_password == 1:
                    print("Last chance!")
        elif password_verification.lower() in "no":
            print("Ok!")
    elif password == saved_password and not username == saved_username:
        username_verification = input("Wrong username,try again? ")
        if username_verification.lower() in "yes":
            tries_username = 5
            while tries_username > 0:
                username = input("Username: ")
                tries_username -= 1
                if username == saved_username:
                    print("Welcome back " + saved_username + "!")
                elif username != saved_username and not username == 1:
                    print("Wrong password!")
                elif username == 1:
                    print("Last chance!")
        elif username_verification.lower() in "no":
            print("Ok!")
    else:
         print("Wrong username and password!")

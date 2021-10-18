
from Account_Creation_Simple import accountCreation
from Account_Creation_Simple import accountVerification
account_existence = input('Do you have an account? ')
# checks if the user has an account or not
if account_existence.lower() in "yes":
    accountVerification()
elif account_existence.lower() in "no":
    account_making_process = input("Do you want to make an account? ")
    if account_making_process.lower() in "no":
        print("Ok!")
        # makes the account via overwriting in the respective file
    elif account_making_process.lower() in "yes":
        accountCreation()
else:
    print('Invalid response!')

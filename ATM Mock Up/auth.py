import random
import validation
import database

#database = {}

def init():
    print("Welcome to BankPHP")
    
    try:
        haveAccount = int(input('Do you have account with us:\n 1 (yes) \n 2 (no)\n'))
    except ValueError:
        print('Selected option is not a number')
        init()
        
    if(haveAccount == 1):
        login()
    elif(haveAccount == 2):
        register()
    else:
        print('You have selected an invalid option')
        init()
            
            
      
            
def login():
    print("***********Login**********")
    

    accountNumberFromUser = input("What is your account number? \n")
    
    is_valid_account = validation.account_number_validation(accountNumberFromUser)
    
    if is_valid_account:
        password = input("What is your password? \n")
            
        for accountNumber, userDetails in database.items():
            if accountNumber == int(accountNumberFromUser):
                if(userDetails[3] == password):
                    print('\n')
                    initialAccountBalance(userDetails)
                    bankOperation(userDetails)
                else:
                    print("Invalid acount passsword")
                    login()
    else:
        login()
    
    
def register():
    
    print("***** Registration ****")
    email = input("What is your email address? \n")
    first_name = input("What is your first name \n")
    last_name = input("What is your last name? \n")
    password = input("Create a password for yourself \n")
    confirmPassword = input("confirm password \n")
    
    setPassword = False
    
    while setPassword == False:
        if(password == confirmPassword):
            password = password
            print("password set!")
            
            try:
                accountNumber = generationAccountNumber()
            except:
                print('Account generation failed due to internet error')
                exit()

            
            #database[accountNumber] = [first_name, last_name, email, password,0]

            is_user_created = database.create(accountNumber, [first_name, last_name, email, password, 0])
            
            
            if is_user_created:
                print("Your account has been created!")
                print("\n")
                print("=== ===== ===== ===")
                print("Your account number is %s" % accountNumber)
                print("Make sure you keep it safe")
                print("=== ===== ===== ===")
                setPassword = True
                print("\n")
                login()
                
            else:
                print('Something went wrong')
                register()
        else:
            print("password don't match")
            confirmPassword = input("confirm password \n")

            #print("")
    

def initialAccountBalance(user):
    print(f'Your initial balance is {user[4]}')
    currentAccountBalance = user[4]
    return currentAccountBalance



    
def generationAccountNumber():
    acctNumber = random.randrange(1111111111,9999999999)
    return acctNumber




def bankOperation(user):
    print("welcome %s %s"%(user[0], user[1]))
    
    try:
        selectedOption = int(input("What would you like to do? \n (1) deposit \n (2) withdraw \n (3) check balance \n (4) logout \n (5) exit \n"))
    except:
        print('Selection must be a number')
        bankOperation(user)
        
    if(selectedOption == 1):
        depositOperation()
        
    elif(selectedOption == 2):
        withdrawOperation()
        
    elif(selectedOption == 3):
        for accountName, userDetails in database.items():
            currentBalance(userDetails)
        
    elif(selectedOption == 4):
        logout()
        
    elif(selectedOption == 5):
        print('Thank you for banking with us')
        exit()
        
    else:
        print("Invalid option selected")
        
    
    print("\n")    
    anotherOption = int(input("would you like to do something else? \n (1) Yes \n (2) No \n"))
    if (anotherOption == 1):
        print("\n")
        bankOperation(user)
    elif (anotherOption == 2):
        print('Thank you for banking with us')
        exit()
    else:
        print("Invalid option selected")



# def checkBalance():
#     for accountName, userDetails in database.items():
#         if depositOperation() is not None:
#             return currentBalance(userDetails) + depositOperation()
#         else:
#             return currentBalance(userDetails)

def currentBalance(user):
    print(f'Your current account balance is {user[4]}')


    
def depositOperation():
    for accountName, userDetails in database.items():
        deposit = int(input('How much would you like to deposit: \n'))
        userDetails[4]+=deposit
        print("The sum of %s has been deposited into your account" % deposit)
        print('Your current balance is %s'% userDetails[4]) 
    # def returnDeposit():
    #     summation = (int(currentBalance(userDetails))+deposit)
    #     return summation
    # return returnDeposit()



def withdrawOperation():
    for accountName, userDetails in database.items():
        print[f'Your balance is {userDetails[4]}']
        cash = int(input('How much would you like to withdraw\n'))
        if confirmCheck(cash):
            userDetails[4] -= cash
            print(f'You have successfully withdrawn {cash} \n')
        else:
            print('Insuffiecient fund') 
        
    
def confirmCheck(amount):
    for accountName, userDetails in database.items():
        if userDetails[4] >= amount:
            return True
    return False
         
    
    
def logout():
    login()
    
    
init()

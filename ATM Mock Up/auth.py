import random
import validation

database = {}

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

            
            database[accountNumber] = [first_name, last_name, email, password]

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
            print("password don't match")
            confirmPassword = input("confirm password \n")

            #print("")
    
    



    
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
        checkBalance()
        
    elif(selectedOption == 4):
        logout()
        
    elif(selectedOption == 5):
        exit()
        
    else:
        print("Invalid option selected")
        
    
    print("\n")    
    anotherOption = int(input("would you like to do something else? \n (1) Yes \n (2) No \n"))
    if (anotherOption == 1):
        print("\n")
        bankOperation(user)
    elif (anotherOption == 2):
        exit()
    else:
        print("Invalid option selected")





def checkBalance():
    current_balance = 0
    current_balance += depositOperation()
    print('Your current balance is %s' % current_balance)

    
def depositOperation():
    deposit = int(input('How much would you like to deposit: \n'))
    print("The sum of %s has been deposited into your account" % deposit)
    return deposit


def withdrawOperation():
    cash = int(input('How much would you like to withdraw'))
    if confirmCheck(cash):
        print(f'You have successfully withdrawn {cash} \n')
    else:
        print('Insuffiecient fund') 
    
    
def confirmCheck(amount):
    if depositOperation() >= amount:
        return True
    return False
         
    
    
def logout():
    login()
    
    
init()

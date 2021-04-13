import time
name = input("enter name: \n")
allowedUsers = ['Seyi', 'Mike', 'Love']
allowedPassword = ['passwordSeyi', 'passwordMike', 'passwordLove']

if (name in allowedUsers):
    password = input("enter password: \n")
    userId = allowedUsers.index(name)
    
    if (password == allowedPassword[userId]):
        print(' ')
        date = time.strftime('%A, %B %d %Y')
        time = time.strftime('%H:%M')
        print(date)
        print(time)
        print(' ')
        print('Welcome %s' %name)
        print('*********************************')
        print('these are the available options:')
        print('2. Withdrawal')
        print('3. Cash Deposit')
        print('4. Complaint')
        print(' ')
        
        selectedOptions = int(input('pls select an option: \n'))
        
        if (selectedOptions == 1):
            cash = int(input('How much would you like to withdraw'))
            print('Take your cash \n')
             
    
        elif (selectedOptions == 2):
            current_balance = 0
            deposit = int(input('How much would you like to deposit: \n'))
            current_balance += deposit 
            print('Your current balance is %s' %current_balance)
             
    
        elif (selectedOptions == 3):
            report = input('What will you like to report? \n')
            print('Thank you for contacting us')
             
    
        else:
            print('invalided option selected, please try again')
        
    else:
        print("password incorrect, please try again")
        
        
else:
    print("name not found, please try again")

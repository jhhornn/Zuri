#Create record
#Read record
#Update record
#Delete record

#CRUD
import os

# file = os.getcwd()

user_db_path = "ATM Mock Up/dbhnjgbhata/user_record/"

def create(account_number, user_details):
    completion_state = False
    try:
        # create a file, name of the file would be account_number.txt
        f = open(user_db_path + str(account_number) + ".txt", "w+")
        
    except FileExistsError:
        print('User already exists')
        #delete the already created file, and print out
        delete(account_number)
        
    
    else:
        f.write(str(user_details))  # add the user details to the file
        completion_state = True

    finally:
        f.close() #always close files opened
        #return true
        return completion_state
    
def read(user_account_number):
    print('Read record')
    #find user with the account number
    #
    
def update(user_account_number):
    print('Update record')
    #find the user with teh account number
    #fetch content of file
    #update the content of the file
    
def delete(user_account_number):
    print('Delete record')
    #find user with account number
    #delete account user record
    #return True
    
    is_delete_successful = False
    
    if os.path.exists(user_db_path + str(user_account_number)):
        try:
            os.remove(user_db_path + str(user_account_number) + ".txt")
            is_delete_successful = True
        
        except FileNotFoundError:
            print('User not found')
        
        finally:    
            return is_delete_successful        
    
        
def find(user_account_number):
    print('find user')
    
    
    #find user record in the data file

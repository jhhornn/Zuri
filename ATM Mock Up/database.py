#Create record
#Read record
#Update record
#Delete record

#CRUD
import os
import validation

# file = os.getcwd()

user_db_path = "ATM Mock Up/data/user_record/"

def create(account_number, first_name, last_name, email, password):
    
    user_data = first_name + "," + last_name + "," + email + "," + password + "," + str(0)

    if does_account_number_exist(account_number):
        return False
    
    if does_email_exist(email):
        print('User already exists')
        return False
    
    completion_state = False
    try:
        # create a file, name of the file would be account_number.txt
        f = open(user_db_path + str(account_number) + ".txt", "w+")
        
    except FileExistsError:
        does_file_contain_data = read(user_db_path + str(account_number) + ".txt")
        if not does_file_contain_data:
            delete(account_number)
        #delete the already created file, and print out
        #delete(account_number)
        
    
    else:
        f.write(str(user_data))  # add the user details to the file
        completion_state = True

    finally:
        f.close() #always close files opened
        #return true
        return completion_state
    
def read(user_account_number):
    #find user with the account number
    #fetch content from file
    
    is_valid_account_number = validation.account_number_validation(user_account_number)
    
    try:
        if is_valid_account_number:
            f = open(user_db_path + str(user_account_number) + ".txt", "r")
        
        else:
            f = open(user_db_path + str(user_account_number), "r")
        
    except FileNotFoundError:
        print('User not found')
        
    except FileExistsError:
        print("User doesn't exist")
        
    except TypeError:
        print('Invalid account number format')
        
    finally:    
        return f.readline()
    
    return False

    
def update(user_account_number):
    if does_account_number_exist(user_account_number):
        read(user_account_number)
    
    
    
    print('Update record')
    #find the user with the account number
    #fetch content of file
    #update the content of the file
    
def delete(user_account_number):
    print('Delete record')
    #find user with account number
    #delete account user record
    #return True
    
    is_delete_successful = False
    
    if os.path.exists(user_db_path + str(user_account_number) + ".txt"):
        try:
            os.remove(user_db_path + str(user_account_number) + ".txt")
            is_delete_successful = True
        
        except FileNotFoundError:
            print('User not found')
        
        finally:    
            return is_delete_successful        
    
        
def does_email_exist(email):
    all_users = os.listdir(user_db_path)
    
    for user in all_users:
        #print(user[:10])
        user_list = str.split(read(user[:10]), ',')
        if email in user_list:
            return True
    return False    


def does_account_number_exist(account_number):
    all_users = os.listdir(user_db_path)

    for user in all_users:
        if user in str(account_number) + ".txt":
            return True
    return False
    
    
    #find user record in the data file 
    #check for duplicate email
    
    
def authenticated_user(account_number, password):
    if does_account_number_exist(account_number):
        user = str.split(read(account_number), ',')
        if password == user[3]:
            return user 
        
    return False 


def print_list(account_number):
    all_users = os.listdir(user_db_path)

    for user in all_users:
        if user[:10] == account_number: 
            user_list = str.split(read(user[:10]), ',')
            return user_list
    return False


def print_amount(account_number):
    return int(print_list(account_number)[4])

# does_email_exist('awosiseo@gmail.com')
# does_account_number_exist(1235380413)
# print(print_list(3601341816))
# print(print_amount())

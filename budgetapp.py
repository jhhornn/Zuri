
class Budget():
    
    def __init__(self, name):
        self.name = name
        self.ledger = list()
        
        
    def deposit(self, description=""):
        amount = int(input(f"How much will you like to deposit in your {description} account?\n"))
        self.ledger.append({'amount':amount, 'description':description})
        print(f"You have successfully deposited {amount} in your {description} account")
        
    def withdraw(self, description=""):
        amount = int(input(f"How much will you like to withdraw for {description} from {self.name} account\n"))
        if(self.check_funds(amount)):
            self.ledger.append({'amount':-amount, 'description':description})
            print(f"You have successfully withdrawn {amount} for {description}")
        else:
            print("insufficient funds")
    
    def get_balance(self):
        total_cash = 0
        for item in self.ledger:
            total_cash += item['amount']
        return total_cash
    
    def transfer(self, category):
        amount = int(input(f"How much will you like to transfer from {self.name}\n"))
        if(self.check_funds(amount)):
            self.ledger.append({'amount': -amount, 'description': self.name})
            category.ledger.append({'amount': amount, 'description': category.name})
            #self.get_balance = (self.get_balance() - amount)
            #category.deposit = amount
            print(f"{amount} has been successfully transfered from {self.name} to {category.name}")
        else:
             print("Insufficient fund") 
    
    def check_funds(self, amount):
        if(self.get_balance() >= amount):
            return True
        return False
    
    def summary(self):
        print("**********Summary**********")
        for item in self.ledger:
            print(f"{item['description']} ------- {item['amount']}")
        print(f"Total amount left:{self.get_balance()}")
        
    
    
    
food = Budget('food')
Clothings = Budget('clothings')

Clothings.deposit('clothings')
Clothings.withdraw('shirt')
Clothings.withdraw('trousers')
Clothings.withdraw('face cap')
Clothings.transfer(food)


food.withdraw('grocery')
food.withdraw('foodstuff')

Clothings.summary()
food.summary()


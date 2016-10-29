#fionn mcguire
#C13316356
# Creating a class to hold the bank information
class Bank:
    # Filling in the  bank deatils
    def __init__(self, Account, AccountType, TransactionType, Debit, Credit, Balance):
        self.account = Account
        self.accountType = AccountType
        self.transactionType = TransactionType
        self.debit = Debit
        self.credit = Credit
        self.balance = Balance

    # Printing out the bank details
    def show(self):
        print("Account\t\t %s" %self.account)
        print("Account Type\t %s" %self.accountType)
        print("Transaction\t %s" %self.transactionType)
        print("Debit\t\t %s" %self.debit)
        print("Credit\t\t %s" %self.credit)
        print("Balance\t\t %s\n" %self.balance)
        
# Making a class to hold the customers details 
class Customer:
    # Initilizing the class and putting in the customers information 
    def __init__(self, name, email, x):
        self.name = name
        self.email = email
        self.customer_id = str(x)

    # Printing out the customers information
    def show(self):
        print("Name\t\t %s" %self.name)
        print("Email\t\t %s" %self.email)
        print("Customer ID\t %s\n" %self.customer_id)

# Creating a class to hold the account information
class Account:
    # Filling up the account with the persons details
    def __init__(self,account_num, customer, balance, credit_limit, interest_rate ):
        self.account_num = account_num
        self.customer = customer
        self.balance = balance
        self.credit_limit = 0
        if(credit_limit != 0):
                self.credit_limit = credit_limit
        self.interest_rate = interest_rate

    def show(self):
        # Neatly printing out the Account information
        print("Account No \t %s" %self.account_num)
        print("Customer\t %s" %self.customer)
        print("Balance    \t %s" %self.balance)
        print("Credit Limit\t %s" %self.credit_limit)
        print("Interest Rate\t %s\n" %self.interest_rate)
        print("------------------------------------------")


x = 56
# Putting in the relevant information about the person account 
c1 = Customer('John Smith', 'johnsmith@gmail.com', x)
a1 = Account(x, 0, 0, 0, 0.056)
b1 = Bank(x, 'Current', 'Opening', 0, 500, 500)
# Making the Account ID/Customer ID/Count move on a number
x+=1

c2 = Customer('Martin Reilly', 'martinr1@hotmail.com', x)
a2 = Account(x, 0, 1560, 0, 0.023)
b2 = Bank(x, 'Current', 'Withdraw', 360, 0, 1260)
x+=1

c3 = Customer('Phil Tully', 'tully16@gmail.com', x)
a3 = Account(x, 0, 3200, 0, 0.785)
b3 = Bank(x, 'Debit', 'Lodge', 700, 500, 3000)
x+=1

# Calling the show part of each class to display the person and their account information
c1.show()
b1.show()
a1.show()

c2.show()
b2.show()
a2.show()

c3.show()
b3.show()
a3.show()

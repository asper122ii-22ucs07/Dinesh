def__init__(self, account-number, account_holder_name,initial_balance=0.0)
self. __account_number=account_number
self.__account_holder_name=account_holder_name
self.__account_balance=initial_balance:float
self.__account_balance=initial_balance
def deposit(self,amount):
  if amount>0:
    self.__account_balance+=amount
    print("Deposited€{}.New balance:€{}".format(amount,self.__account_balance))
  else:
    print("Invalid deposit amount. please deposited a positive amount. ")
    def withdraw(self,amount):
      if amount>0 and amount<=self.__account_balance:
       self.__account_balance_=amount
        print("withdraw€{}.New balance:€{}."format(amount,self.__account_balance))
      else:
        print("Invalid withdrawal amount or insufficient balance. ")
        def display_balance(self):
          print(" balance for{}(Account#{}):€{}".format)
          self.__account_holder_name,self.__account_number,
          self.__account_balance))
          ?
  account=BankAccount(account_number="123456789i"
                     account_holder_name="Hari prabu", 
          
    
# class human:
#     def __init__(self, name="abcd",age=30):
#         self.name=name
#         self.age=age
#     def greet(self):
#         print(f"Hello, my name is {self.name} and  Iam {self.age} years old.")
    

# person1=human("hari",25)

# person2=human("Abhi",24)

# person3=human()

# person1.greet()
# person2.greet()
# person3.greet()








# #Constructor--------- __init__(self,parameters)

# #It is a special method in python that initiates an object when it is created.




class bankAccount:
    def __init__(self, balance):
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print("Deposited=",amount)
    def withdraw(self,amount):
        self.balance-=amount
        print("Withdraw amount=",amount)
    def check_balance(self):
        print("Balance amount=",self.balance)
    
person1=bankAccount(1000)

person1.check_balance()

person2=bankAccount(2000)
person2.check_balance()

person1.deposit(10000)


person1.check_balance()

person1.withdraw(5000)

person1.check_balance()
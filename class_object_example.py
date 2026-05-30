# # # class human:
# # #     def __init__(self, name="abcd",age=30):
# # #         self.name=name
# # #         self.age=age
# # #     def greet(self):
# # #         print(f"Hello, my name is {self.name} and  Iam {self.age} years old.")
    

# # # person1=human("hari",25)

# # # person2=human("Abhi",24)

# # # person3=human()

# # # person1.greet()
# # # person2.greet()
# # # person3.greet()








# # # #Constructor--------- __init__(self,parameters)

# # # #It is a special method in python that initiates an object when it is created.




# # class bankAccount:
# #     def __init__(self, balance):
# #         self.balance=balance

# #     def deposit(self,amount):
# #         self.balance+=amount
# #         print("Deposited=",amount)
# #     def withdraw(self,amount):
# #         self.balance-=amount
# #         print("Withdraw amount=",amount)
# #     def check_balance(self):
# #         print("Balance amount=",self.balance)
    
# # person1=bankAccount(1000)

# # person1.check_balance()

# # person2=bankAccount(2000)
# # person2.check_balance()

# # person1.deposit(10000)


# # person1.check_balance()

# # person1.withdraw(5000)

# # person1.check_balance()



# # class employee:
# #     def __init__(self,name,basic_salary):
# #         self.name=name
# #         self.basic_salary=basic_salary

# #     def total_salary(self):
# #         hra=self.basic_salary*0.30
# #         da= self.basic_salary*0.10
# #         total=self.basic_salary+hra+da
# #         print(f"Employee name {self.name}")
# #         print(f"Total Salary= {total}")
    

# # e1=employee("Abhi",30000)
# # e2=employee("Hari",25000)

# # e1.total_salary()

# # e2.total_salary()


# class calculator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def addition(self):
#         c=self.a+self.b
#         print(f"Addition value={c}")
    
#     def substraction(self):
#         d=self.a-self.b
#         print(f"Substraction value={d}")

#     def multiplication(self):
#         e=self.a*self.b
#         print(f"Multiplication value={e}")
    
#     def division(self):
#         f=self.a/self.b
#         print(f"Quotient value={f}")
    


# x=calculator(10,4)

# x.addition()
# x.substraction()


















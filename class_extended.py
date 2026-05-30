#Pillars of OOP(Object oriented programming)
    
#     1.Inheritance
#     2.Polymorphism
#     3.Abstraction
#     4.Encapsulation
    

    
#     Inheritance

#         1. Base class(parent class)
#         2. Derived class(child class)

#         1) single inheritance

#             class A:
#                 #properties methods

#             class B(A):
#                 #properties and methods from A

#         2)Multi level inheritance

#             class A:
#                 #properties methods

#             class B(A):
#                 #properties and methods from A

#             class C(B):
#                 #properties and methods from B
            
#             class D(C):
#                 #properties and methods from C
            
#         3) Multiple inheritance

#             class A:
#                 #properties and methods
#             class B:
#                 #properties and methods
#             class C(A,B):
#                 #properties and methods from A and B
        
#         3)Hierarchical inheritance

#             class A:
#                 #properties and methods
#             class B(A):
#                 #properties and methods from A
#             class C(A):
#                 #properties and methods from A


#         4)Hybrid Inheritance

#             class A:

#             class B(A):
            

#             class C(A):

#             class D(A,B):

# '''

    
# class family:
#     def __init__(self,family_name):
#         self.family_name=family_name
#     def display(self):
#         print(f"{self.family_name}")

# class child(family):
#     def __init__(self,family_name,name):
#         super().__init__(family_name)
#         self.name=name
#     def display(self):
#         super().display()

# c=child("king","abcd")
# c.display()
# # print(c.family_name)
# # print(c.name)




# class employee:
#     def __init__(self,name):
#         self.name=name
#     def display(self):
#         print(f"Employee name is {self.name}")

# class developer(employee):

#     def code(self):
#         print(f"{self.name} is writing code")

# class developer2(developer):
#     def testing(self):
#         print(f"{self.name} is testing")
    
# d=developer2("abcd")
# d.display()
# d.code()
# d.testing()


# class father:
#     def work(self):
#         print("father is working")
    
# class mother:
#     def cooking(self):
#         print("Mother is cooking")

# class child(father,mother):
#     pass

# c=child()

# c.work()
# c.cooking()









class parent:
    def work(self):
        print("parent is working")

class child1(parent):
    pass

class child2(parent):
    pass

c1=child1()
c2=child2()

c1.work()
c2.work()
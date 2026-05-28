class human:
    def __init__(self, name="abcd",age=30):
        self.name=name
        self.age=age
    def greet(self):
        print(f"Hello, my name is {self.name} and  Iam {self.age} years old.")
    

person1=human("hari",25)

person2=human("Abhi",24)

person3=human()

person1.greet()
person2.greet()
person3.greet()








#Constructor--------- __init__(self,parameters)

#It is a special method in python that initiates an object when it is created.















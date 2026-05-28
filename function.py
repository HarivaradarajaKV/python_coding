# # a=int(input("Enter the value of a: "))
# # b=int(input("Enter the value of b: "))

# # c=a+b

# # print("The sum of a and b is: ",c)


# #Function--- A function is a block of code  that performs a specific task when called.
# #Function

# #How to define a function in python?

# #syntax of function definition
# #def function_name(parametes/arguments/function inputs):
#     #Block of code


# #How to call a function in python?

# #function_name(values for parameters/arguments/function inputs)




# x=int(input("Enter the value of a: "))
# y=int(input("Enter the value of b: "))


# def sum1(a,b):
#     print("The sum of a and b is: ",a+b)



# print("Welcome to python programming")






# sum1(x,y) # a=x, b=y



# sum1(100,200)



# # x=a+b
# # print("Sum of two variables is: ",x)



# def multiplication_table(num):
#     for i in range(1,11):
#         print(f"{num}X{i}={num*i}")


# print("here i am printing 2 tables")

# n=int(input("Enter the value to generate tables: "))
# multiplication_table(n)

# print("I am printing 10 tables")

# x=int(input("Enter the value to generate tables"))

# multiplication_table(x)


# range(0,1)

# list1=list(range(1,20))

# print(list1)

# def sum1(a,b):
#     print(a+b)



# sum1(1,2)

# x=sum1(2,6)

# print(x)



# def sum2(a,b):
#     return a+b


# sum2(5,7) #-------->a=5, b=7

# x=sum2(6,4)

# print(x)
# print(sum2(7,9))



# def variable(a,b):
#     print("Hello, how are you")
#     x=20 #variable(local variable)




# variable(1,2)





# a=20 #Global variable
# print(a)
# print(x)


# x=30
# def variable(a,b):
#     x=20
#     print("This is example of how local and global variables work")
#     print(x)
#     # print(x)



# variable()
# print(x)


# def function1(name="hari"):
#     print(f"Hello {name}. How are you")


# function1()
# function1("Abhi")


# def multiply(a,b):
#     print(a/b)




# multiply(b=2,a=4)




# def function1(a):
#     print(a)


# function1((1,2,3,4))

# #Variable -lenght arguments

# #  *args and **kwargs

# def function2(*a):
#     print(type(a))
#     print(a)

# function2(1,2,3,4,5,6,7,8)

# def function3(**k):
#     print(k)
#     print(type(k))


# function3(a="hari",b=4,c=5,f="s",k=1.2)

# s="i am studying python"
# x=s.split()
# print(x)
# print(type(x))


# def add1(a,b):
#     return a+b
# add1(1,2)
# #lambda function - It is a small ananymos function that can take any number of arguments but has only one expression

# #syntax

# #lambda arguments: expression

# x=lambda a,b:a+b
# print(x(1,2))



# a=10
# b=20
# print(a+b)





#recursion-It occurs when function call itself


# def factorial(num):
#     fact=1
#     for i in range(1,num+1):
#         fact=fact*i
#     print(fact)


# factorial(1)

# factorial(10)


def factorial_recursion(n):
    if(n==1):
        return 1
    else:
        return n* factorial_recursion(n-1)

print(factorial_recursion(5))


# (a+b)^=a^2 +b^2+2ab

# 5!  == 5x4x3x2x1
# n!  == nx(n-1)x(n-2)x(n-3)X(n-4)...........(n-1)
#         5X4X3X2X1
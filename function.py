#1. Simple Function (No Parameters, No Return Value)
def greet():
    print("Hello good morning")
#calling function
greet()

#2. Function with Parameters
def greet(name):
    print("Hello",{name})
#calling function
greet("Alice")
greet("neeta")

#3. Function with a Return Value
def square(num):
    return num*num
result=square(4)
print(result)

# A lambda function in Python is a small anonymous function.
# It is used when you need a quick function for a short period and don’t want to formally define it with def.

#  Syntax of Lambda Function:

# lambda arguments: expression
square = lambda x :x*x
print(square(5))

#add using lambda 
add = lambda a, b: a + b
print(add(3, 7))
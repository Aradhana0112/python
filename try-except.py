#try:
     #code that might cause error
#except Exceptiontype:
     #code to handel error
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# try:
#     num=int(input("enter a number: "))
#     result=10 / num
#     print("Result", result)
# except ZeroDivisionError:
#     print("Error: Cannot divided by zero")
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number.")
else:
    print("You entered:", x)

print('Hello, world!')
My_Varriable = 10
print(My_Varriable)
print(type(My_Varriable))
print(id(My_Varriable))

# # Lets create a Calculator in Python that can add, subtract, multiply and divide two numbers
# def add(x, y):
#     return x + y
#     def subtract(x, y):
#         return x - y
#     def multiply(x, y):
#         return x * y
#     def divide(x, y):
#         if y == 0:
#             return ValueError('Cannot divided by Zero')
#             return x / y
#             print("Select Operations -\n ")
#             print("1. Add")
#             print("2. Subtract")
#             print("3. Multiply")
#             print("4. Divide")
#             choice = input("Enter choice(1/2/3/4): ")
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))
#             if choice == '1':
#                 print(num1, "+", num2, "=", add(num1, num2))
#             elif choice == '2':
#                 print(num1, "-", num2, "=", subtract(num1, num2))
#             elif choice == '3':
#                 print(num1, "*", num2, "=", multiply(num1, num2))
#             elif choice == '4':
#                 print(num1, "/", num2, "=", divide(num1, num2))
#             else:
#                 print("Invalid input")
                
                # Calculator in Python

# Functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by Zero"
    return x / y

# Menu
print("Select Operation -\n")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# User choice
choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Logic
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid Input")

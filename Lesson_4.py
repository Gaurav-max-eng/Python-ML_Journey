# Lesson 4 - Functions
# Name : Gaurav
# Date : 29 March 2026

# 1 . Function Without input
def greet():
    print("Hello! Welcome to python programming learning.")

# 2 . Function which takes input
def greet_with_name(name):
    print("Hello!", name, "Welcome to python learning")

# 3 . Function which takes input input and return value
def add(a,b):
    return a+b

def Multiply(a,b):
    return(a*b)

# 4 . Function with default value 
def power(base,exponent=2):
    return(base ** exponent)

# 5 . passing inputs to function

num_1 = int(input("Enter the First Number"))
num_2 = int(input("Enter the Second Number"))
Result_1 = add(num_1,num_2)
print(f"The addition of the numbers are: {Result_1}")

num_3 = int(input("Enter the First Number"))
num_4 = int(input("Enter the Second Number"))
Result_2 = Multiply(num_3,num_4)
print(f"The Multiplications of the numbers are: {Result_2}")

num_5 = int(input("Enter the base"))
Result_3 = power(num_5)
print(f"The base to the power 2 is 55: {Result_3}")

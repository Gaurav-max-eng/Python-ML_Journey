# Lesson 2 - Input, Operators and if-else
# Name: Gaurav
# Date: 28 March 2026

# 1. Taking input from user
name = input("What is your name? ")
age = int(input("How old are you? "))
height = float(input("What is your height in feet?"))

print("\n-- Your information ---")
print("Name :", name)
print("Age :", age)
print("Height :", height)

# 2. Basic Operators (calculations)
print("\n-- Calculations ---")
print("Age after 2 years  :", age + 2)
print("Double height  :", height * 2)
print("Age + Height :", age + height)

# 3. if-else (making decisions)
if age>= 18:
    print("You are an adult")
else:
    print("You are still a minor")

if height > 5.5:
    print("You are tall")
else:
    print("You have average height")  

# Bonus: Comparison operators
if age == 20:
    print("Same age as me!")
elif age >20:
    print("You are older than me")
else:
    print("You are younger than me")    

#Lesson 3 - Loops and Lists
# Name: Gaurav
# Date: 28 March 2026

# 1. Lists (multiple values together)
fruits = ["Apple", "Banana", "Mango", "Orange"]
numbers = [10,20,30,40,50]
mixed = ["Gaurav", 20,5.8,True]

print("Fruits;", fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Total fruit:", len(fruits))

# 2. For Loop (list individual items)
print("\n-- For Loop on List ---")
for fruit in fruits:
    print("I like", fruit)

print("\n--- For Loop with range ---")
for i in range(5):
    print("Number:",i)

# 3. While Loop
print("\n--- While Loop ---")
count = 1
while count <= 5:
    print("Count is", count)
    count = count + 1


# Bonus: Create a new list using loop
squares = []
for i in range(1,6):
    squares.append(i * i)
print("Squares list:", squares)


# 4. Mini Project: Simple Number Guessing Game
print ("n\--- Mini Project: Guess the Number ---")
secret_number = 7
guess = int(input("Guess a number between 1 to 10: "))
if guess == secret_number:
    print("Correct! You won")
elif guess> secret_number:
    print("Too high!")
else:
    print("Too low!")
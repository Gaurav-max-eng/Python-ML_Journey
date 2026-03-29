# Mini Project

# 1 . Simple Calculator
def calculator():
 
 print("\n Choose your operation ")
 print("\n 1. Addition")
 print("\n 2. Subtraction")
 print("\n 3. Multiplication")
 print("\n 4. Division")
 print("\n 5. Modulo")

 choice = int(input())

 num_1 = int(input("Enter the First Number : "))
 num_2 = int(input("Enter the Second Number : "))
 
 if choice == 1:
  return num_1 + num_2
 
 elif choice == 2:
  return num_1 - num_2
 
 elif choice == 3:
  return num_1 * num_2
 
 elif choice == 4:
  return num_1 / num_2
 
 elif choice == 5:
  if num_2 == 0:
   return ("Division not possible ")
  return num_1 % num_2
 
 else:
  print("Invalid choice")


Result = calculator()
print(f"Final Result : {Result}") 




 
 
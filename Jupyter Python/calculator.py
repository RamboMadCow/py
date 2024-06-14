import math

print("""
      
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponent
6. Calculate BMI
7. Calculate the area of a triangle
8. Calculate the area of a square
9. Finding the square of a root
      
      
      
    
""")

Operation = int(input("Please chose the operation you'd like to do: "))

if Operation == 1:
    Number_1 = int(input("Please enter in the first number: "))
    Number_2 = int(input("Please enter in the second number: "))
    
    print ("Results: ", Number_1 + Number_2)
    
elif Operation == 2:
    Number_1 = int(input("Please enter in the first number: "))
    Number_2 = int(input("Please enter in the second number: "))
    
    print ("Results: ", Number_1 - Number_2)
    
elif Operation == 3:
    Number_1 = int(input("Please enter in the first number: "))
    Number_2 = int(input("Please enter in the second number: "))
    
    print ("Results: ", Number_1 * Number_2)
    
elif Operation == 4:
    Number_1 = int(input("Please enter in the first number: "))
    Number_2 = int(input("Please enter in the second number: "))
    
    print ("Results: ", Number_1 / Number_2)
    
elif Operation == 5:
    Number_1 = int(input("Please enter in the first number: "))
    Number_2 = int(input("Please enter in the second number: "))
    
    print ("Results: ", Number_1 ** Number_2)
    
    
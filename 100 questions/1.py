# # # Add to Number 
# n1 = int(input("Enter a Number "))
# n2 = int(input("Enter a Number "))

# print(f'Sum of Two Number is {n1+n2}')

# ?# #Hello world
# print("Hello World")

# # # Square root
# num = int(input("Enter the number "))

# sq = num**0.5

# print(f"Square Root of {num} is {sq}")

# # # Area of Triangle

# heigth = int(input("Enter the height of Triangle "))
# base = int(input("Enter the Base of Triangle "))

# area = (heigth*base)/2

# print(f"Area of triangle is {area}")

# # Swap Two Variables
# a = 10 
# b = 20 

# a,b = b,a
# # temp = a
# # a = b
# # b = temp

# print(f"A {a} and B {b}")

# # Convert to Km to mile

# km = 12
# mile = km*0.621371

# print(f"KM {km} to Mile {mile}")

# # Is no. is positive Negative or Zero
# num = int(input("Enter the number "))
# if num>=0:
#     print("Number is Positive")
# else:
#     print("Number is negative ")

# # Is a Number is Odd or Even
# num = int(input("Enter the number "))
# if num%2==0:
#     print("Number is Even")
# else:
#     print("Number is Odd ")

# # Leep Year or not

# num = int(input("Enter the year "))
# if (num % 400 == 0) or (num % 4 == 0 and num%100 == 0):
#     print("Leap Year")
    
# else:
#      print("Not a leep Year")

# the Largest Among Three Numbers

num1 = int(input("Enter the frist Number "))
num2 = int(input("Enter the Second Number "))
num3 = int(input("Enter the Thrid Number "))

if num1 > num2 and num1 > num3:
    print(f"{num1} is Frist Largest ")
elif num2 > num3:
    print(f"{num2} is Second Largest ")
else:
    print(f"{num3} is Thrid Largest ")
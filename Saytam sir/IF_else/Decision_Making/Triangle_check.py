num1 = int(input("Enter the number "))
num2 = int(input("Enter the number "))
num3 = int(input("Enter the number "))

if num1 == num2 == num3:
    print("Equlileral")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("Isosceles")
else:
    print("Scalene")
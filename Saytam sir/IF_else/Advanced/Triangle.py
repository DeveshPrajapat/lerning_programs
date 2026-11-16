num1 = int(input("Enter the number 1 "))
num2 = int(input("Enter the number 2 "))
num3 = int(input("Enter the number 3 "))

if (num1+num2)>num3 and (num1+num3)>num2 and (num2+num3)>num1:
    print("Valid Triangle")
else:
    print("Not Valid Triangle")
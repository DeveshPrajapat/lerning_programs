num1 = int(input("Enter the number "))
num2 = int(input("Enter the number "))
num3= int(input("Enter the number "))

if num1 > num2  :
    if num1 > num3:
        print(f"Number {num1} maximum ")
    else:
        print(f"Number {num2} Maximum")
else:
    if num2 > num3:
        print(f"Number {num2} Maximum")
    else:
        print(f"Number {num3} Maximum")
   
    
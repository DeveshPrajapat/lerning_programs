num = int(input("Enter the number "))

if num%400 ==0 or (num%4 == 0 and num%100 !=0):
    print(f"Leap Year")
else:
    print("Not a leap Year")
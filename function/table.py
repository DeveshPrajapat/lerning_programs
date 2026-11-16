def table (a,b):    
    for j in range (1,11):
        for i in range (a,b+1):
            print(f"{j} * {i} = {j*i}".ljust(15),end="")
        print()

num = int(input("Enter any number "))
num2 = int(input("Enter 2nd numner "))

table(num,num2)
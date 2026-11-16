p = 0 
n = 0 
z = 0
while True:
    print("Do you want to Exit \n Yes \n NO")
    k = input("Enter you choices ")
    if "yes" == k:
        break
    elif "no" == k:
        num = int(input("Enter any number "))
        if num > 0:
            p+=1
        elif num < 0 :
            n +=1
        else:
            z +=1
    else:
        print("Default Number ")
            
print(f"Positive number is {p}")
print(f"negative number is {n}")
print(f"zero number is {z}")
         
         

    
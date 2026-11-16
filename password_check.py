password = input("Enter your password ")
c = 0
k =0 
s =0
n = 0
sp =0

for i in password :
    c+=1
    if 'A' <= i <= 'Z':
        print(f"password  has Upper case")
        k +=1 
    elif 'a' <= i <= 'z':
        print(f"password has lower case")
        s +=1
    elif  '0' <= i <='9' :
        print(f"password  has numbers")
        n +=1
    else:
        print(f"password has special ")
        sp +=1
        
print(f"{c} Password length ")

if 6 <= c <=12:
    if k >=1 and s >=1 and n >= 1 and sp >= 1:
        print(f"Password is vaild {password}")
    else:
        print(f" Password is invaild {password}")
else:
        print(f" Password is invaild {password}")
    

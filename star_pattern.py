# #  Rigth side triangle

num = int(input("Enter any number "))
print("Rigth side triangle\n")
for i in range(1,num+1):
    
    for j in range(1,num+1):
        if j<=i:
            print('*',end="")
        else :
            print(' ',end='')
    
    print()

print("------ Next Pattern --------")

#! Rotated Right side triangle
print(" Rotated Rigth side triangle\n")

for i in range (1,num+1):
    for j in range(1,num+1):
        if j>=i:
            print("*",end="")
        else:
            print(" ",end="")
    print()

print("------ Next Pattern --------")

print(" Rigth-Rigth side triangle\n")

for i in range(1,num+1):
    
    for j in range(1,num+1):
        if j<i:
            print('',end="")
        else :
            print('*',end='')
    
    print()
print("------ Next Pattern --------")

print(" Left-Rigth side triangle\n")

for i in range (1,num+1):
    for j in range(1,num+1):
        if j<=i:
            print("*",end="")
        else:
            print(" ",end="")
    print()
print("------ Next Pattern --------")
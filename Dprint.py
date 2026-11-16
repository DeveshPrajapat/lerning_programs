# i = int(input("enter i size "))
# j = int(input("enter j size "))
# for k in range(1,i+1):
#     for l in range(1,j+1):
#         if k == 3 and l == 2 :
#             print(" ",end="")
#         else:
#             print(" *",end="")
#     print()

for i in range(1,6):
    for j in range(1,6):
        if j<=i:
            print('*',end="")
        else :
            print(' ',end='')
    
    print()
    

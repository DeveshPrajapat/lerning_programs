# star patterns
'''
n = 5 
print("5 by 5 Star ")
for i in range(5):
    for j in range(5):
        print("*",end="")
    print()
    
    
    '''


# *****
# *****
# *****
# *****
# *****

'''n = 5 
print("Right side Triangle ")
for i in range(1,5+1):
    for j in range(i):
        print("*",end="")
    print()'''


# *
# **
# ***
# ****
# *****

#  n = 5 
# print("Right side Triangle ulata ")
# for i in range(1,n+1):
#     for j in range(n+1-i):
#         print("*",end="")
#     print()
    
# *****
# ****
# ***
# **
# *


# n = 5 
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end="") 
#     print()

#     *
#    **
#   ***
#  ****
# *****

# n = 5 
# for i in range(1,n+1):
#     for j in range(i+1):
#         print(" ",end="")
#     for k in range(n+1-i):
#         print("*",end="") 
#     print()
    
    
#   *****
#    ****
#     ***
#      **
#       *

# n = 5 
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(2*i-1):
#         print("*",end="")
#     print()

#     *
#    ***
#   *****
#  *******
# *********


# n = 5 
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(2*i-1):
#         print("*",end="")
#     print()

# *********
#  *******
#   *****
#    ***
#     *


n = 5
a = 0 
for i in range(n+1):
    print(a,end=" ")
    a,b = b,a+b
# #TODOFibonacci squence Using Recursion

# def finbo(n):
#    if n <= 1:
#        return n
#    else:
#        return finbo(n-1)+finbo(n-2)
       
    
# n = int(input("Enter the n "))

# if n <=0:
#     print("Enter a Positive number")
# else:
#     print("Fibonacci Number ")
#     for i in range(n):
#         print(finbo(i))

# # #! Find the sum of Naturl Using Recursion

# def sum(n):

#     if n <= 1:
#         return n
#     else:
#         return n+sum(n-1)

# n = int(input("Enter the Natural Number "))

# print(sum(n))

# # #? Factorial of Number Using Recursion

# def fact(n):
#     if n == 0:
#         return 1
    
#     return n*fact(n-1)

# n = int(input("Enter the Number "))

# print(fact(n))

##TODO Decimal to Binary

def convert(n):
    if n>1:
        convert(n//2)
    print(n%2,end="")
    
n = int(input("Enter the number "))
convert(n) 
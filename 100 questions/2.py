# # prime Number

# num = int(input("Enter the number "))
# count = 0
# for i in range(2,num):
#     if num % i == 0:
#         count+=1
#         break
# if count == 1 :
#     print("not Prime ")
# else:
#     print("prime")

# #! Random number 
# import random
# rand = random.randint(1,100)
# print(f'Random number is {rand}')


# #TODO print all prime numbers in an interval

# num = int(input("Enter the number "))


# for i in range(1,num+1):
#     for j in range(2,i):
#         if i%j == 0:
#             break
#     else:
#         print(f'Number is prime {i}')


# # ?Factorial of number 

# num = int(input("Enter the number "))
# f = 1
# if num == 0 :
#     print("Factorial is 0")
# else:
#     for i in range(1,num+1):
#         f = f*i   
#     print("factorial of is ", f)

# !# Multiplication Table

# num = int(input("Enter the table number "))

# for i in range(1,11):
#     print(f'{num} * {i} = {num*i}')

# #? Fibonacci Sequence 

# num = int(input("Enter the fibonacci number "))
# a  = 0
# b = 1 
# if num == 1 :
#     print(a)
# else:
#     print(a)
#     print(b)
#     for i in range(2,num):
#         c= a+b
#         a = b
#         b = c 
#         print(c)

## TODOArmstrong Number

# num = int(input("Enter a number "))

# len = len(str(num))
# org = num
# arm = 0
# while num > 0:
#         r = num%10
#         arm += r**len 
#         num = num//10
    
# if org == arm:
#     print(f'{org} is armstrong ')
# else:
#     print(f'{org} is not armstrong ')
        
# #! Armstrong Number
        
# lower = int(input("Enter a Lower limit "))
# upper = int(input("Enter a Upper limit "))

# for i in range(lower,upper+1):
#     l = len(str(i))
#     org = i
#     arm = 0
#     while i > 0:
#         r = i%10
#         arm += r**l
#         i = i//10
    
#     if org == arm:
#         print(f'{org} is armstrong ')
    

# #? Sum of Natural Number is 

# num = int(input("Enter the number "))
# sum = 0
# for i in range(1,num+1):
#     sum+=i
#     print(f"Sum of Natural Number {i}, {sum}")

# #TODO Display Powers of 2 Using Anonymous funtions 
    
# num = int(input("Enter the Number "))
# p = int(input("How many power do you want "))
# for i in range(p):
#     print(f'{num} power of {i} is {num**i}')

# Convert Deciaml to binary ,octal , and Hexadecimal

decimal = int(input("Enter the Decimal Number "))

print(f"The Conversion of decimal Number {decimal} is : ")
print(bin(decimal),"in Binary")
print(oct(decimal),"in Octal")
print(hex(decimal),"in Hexadecimal")
    

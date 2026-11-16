## ASCII Values of Charcter program
# char  = "A"
# print(f"ASCII value of {char} is {ord(char)}")


## !HCF / GCD 

# def findhcf(x,y):
#     if x < y:
#         smaller = x
#     else:
#         smaller = y
    
#     for i in range(1,smaller+1):
#         if x%i == 0 and y%i == 0 :
#             hcf = i
#     return hcf

# x = int(input("Enter the x "))
# y = int(input("Enter the y "))

# print(f"HCF is {x} and {y} is {findhcf(x,y)}")

# #? Find The Factors of a number 

# num = int(input("Enter the number "))

# for i in range(1,num+1):
#     if num%i == 0:
#         print(f"Factors of {num} is {i}")

# #TODO simple Calculator 
# n1 = int(input("Enter the First number "))
# n2 = int(input("Enter the Second number "))
# print("Enter the \n1.ADD\n2.Subtraction\n3.multiple\n4.Divie")

# choice = int(input("Enter your choice from 1-4 : "))
# if choice == 1:
#     print(f"Addition is {n1+n2}")
# elif choice == 2:
#     print(f"Subtraction is {n1-n2}")
# elif choice == 3:
#     print(f"Multiple is {n1*n2}")
# elif choice == 4:
#     print(f"Division is {n1/n2}")
# else:
#     print("Enter Right Number")


# #! Shuffle Deck of Cards

# import random, itertools

# deck = list(itertools.product(range(1,14),["Spade","Club","Hearts","Diamond"]))

# random.shuffle(deck)

# for i in range(5):
    
#     print(deck[i][0]," of ",deck[i][1])

# #? Calendar

# import calendar

# year = int(input("Enter the Year "))
# month = int(input("Enter the Month "))

# cal = calendar.month(year,month)


# print(cal)

    
    
    
    


    
    



    